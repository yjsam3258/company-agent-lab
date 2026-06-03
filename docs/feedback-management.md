# Feedback Management

This document explains how public feedback becomes a safe improvement.

## Feedback Categories

Use these labels:

- `wrong-answer`: the assistant gave a bad answer.
- `ocr`: OCR or table extraction issue.
- `local-ai`: local runtime or model idea.
- `license`: license concern.
- `safety`: privacy or security concern.
- `needs-review`: maintainer must review.
- `eval-candidate`: can become a test case.
- `accepted`: approved for implementation.
- `rejected`: not safe or not useful.

## Triage Flow

```text
New issue
-> Check for private data
-> If unsafe, remove/redact and close
-> If safe, classify label
-> If answer behavior issue, turn into eval
-> Fix lab behavior
-> Run safety scan and eval
-> Merge only if all checks pass
```

## How To Turn Feedback Into Eval

Example:

```powershell
python scripts\add_feedback_eval.py `
  --id community_001 `
  --query "10W 재고 있나?" `
  --route product_search `
  --required "현재고 8개" `
  --required "LUM-SAMPLE-010W-A"
```

Then run:

```powershell
$env:PYTHONDONTWRITEBYTECODE='1'
python scripts\scan_public_safety.py
python scripts\run_eval.py
```

## Private System Transfer Rule

Public feedback can teach a pattern, but it must not directly update the private company AI.

Use this order:

```text
public issue
-> safe lab eval
-> lab fix
-> private review
-> private AEOS gate
-> human approval
```

## Important

If feedback includes private data, do not copy it into evals.

Create a sanitized version instead.
