# Sample Issue Workflow

This file records the first sample feedback workflow.

## Sample Issue To Create

Template:

```text
Wrong answer report
```

Title:

```text
[Wrong Answer]: unclear stock question should still find 10W inventory
```

Labels:

```text
wrong-answer
eval-candidate
needs-review
```

Question:

```text
10 watt stock available?
```

Actual answer:

```text
The lab may fail to understand this form if it only expects "10W".
```

Expected answer:

```text
It should find LUM-SAMPLE-010W-A and show current stock 8.
```

Problem type:

```text
Wrong product match
```

Safe-data check:

```text
No real customer data.
No real ERP data.
No real PDF.
No secret.
Safe to triage.
```

## Maintainer Triage Comment

```text
Thanks. This is safe sample feedback, so I marked it as eval-candidate.

I added a regression eval for this query. The current lab behavior passes the test, so this issue is now covered by CI.
```

## Eval Added

The following eval is already included in `evals/sample_questions.json`:

```json
{
  "id": "community_001_10w_korean_watt",
  "query": "10와트 남아있는 거 있어?",
  "route": "product_search",
  "required": [
    "LUM-SAMPLE-010W-A",
    "현재고 8개"
  ]
}
```

## Verification

Run:

```powershell
$env:PYTHONDONTWRITEBYTECODE='1'
python scripts\scan_public_safety.py
python scripts\scan_license_safety.py
python scripts\run_eval.py
```

Expected:

```text
Public safety scan passed.
License safety scan passed.
Eval passes with community_001_10w_korean_watt included.
```

## Close Rule

Close the issue only after:

- Safety scan passes.
- License scan passes.
- Eval passes.
- The issue is linked to the eval id.
