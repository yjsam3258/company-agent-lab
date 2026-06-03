from __future__ import annotations

import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from company_agent_lab.answer_engine import answer


def main() -> int:
    query = " ".join(sys.argv[1:])
    result = answer(query)
    if "--json" in sys.argv:
        print(json.dumps(result, ensure_ascii=False, indent=2))
    else:
        print(result["answer"])
    return 0 if result.get("ok") else 1


if __name__ == "__main__":
    raise SystemExit(main())
