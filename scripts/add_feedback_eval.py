from __future__ import annotations

import argparse
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
TASKS_PATH = ROOT / "evals" / "sample_questions.json"


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Add a sanitized public feedback item to the sample eval set.")
    parser.add_argument("--id", required=True, help="Stable eval id, for example community_001.")
    parser.add_argument("--query", required=True, help="Sanitized user question.")
    parser.add_argument("--route", required=True, choices=["product_search", "erp_order"], help="Expected answer route.")
    parser.add_argument("--required", action="append", default=[], help="Required text in the answer. Can be repeated.")
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    tasks = json.loads(TASKS_PATH.read_text(encoding="utf-8"))
    if any(task.get("id") == args.id for task in tasks):
        print(f"Eval id already exists: {args.id}")
        return 1
    if not args.required:
        print("At least one --required value is needed.")
        return 1

    tasks.append(
        {
            "id": args.id,
            "query": args.query,
            "route": args.route,
            "required": args.required,
        }
    )
    TASKS_PATH.write_text(json.dumps(tasks, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(f"Added eval: {args.id}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
