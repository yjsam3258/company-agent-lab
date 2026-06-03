from __future__ import annotations

import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from company_agent_lab.answer_engine import answer


ROOT = Path(__file__).resolve().parents[1]
TASKS_PATH = ROOT / "evals" / "sample_questions.json"


def main() -> int:
    tasks = json.loads(TASKS_PATH.read_text(encoding="utf-8"))
    results = []
    for task in tasks:
        response = answer(task["query"])
        text = response.get("answer", "")
        failures = []
        if response.get("route") != task["route"]:
            failures.append(f"route {response.get('route')} != {task['route']}")
        for required in task.get("required", []):
            if required not in text:
                failures.append(f"missing: {required}")
        results.append(
            {
                "id": task["id"],
                "passed": not failures,
                "failures": failures,
                "answer_preview": "\n".join(text.splitlines()[:5]),
            }
        )

    report = {
        "ok": all(item["passed"] for item in results),
        "task_count": len(results),
        "passed_count": sum(1 for item in results if item["passed"]),
        "failed_count": sum(1 for item in results if not item["passed"]),
        "results": results,
    }
    print(json.dumps(report, ensure_ascii=False, indent=2))
    return 0 if report["ok"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
