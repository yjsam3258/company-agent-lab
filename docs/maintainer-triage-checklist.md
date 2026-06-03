# Maintainer Triage Checklist

Use this checklist for every public issue.

## 1. Safety Check

- [ ] No real customer name.
- [ ] No real phone number.
- [ ] No real address.
- [ ] No real ERP screenshot.
- [ ] No real PDF.
- [ ] No API key or token.
- [ ] No private model file.

If unsafe:

```text
Remove or ask the reporter to repost with sanitized data.
Do not copy unsafe content into evals.
```

## 2. Classify

Add labels:

- `wrong-answer`
- `ocr`
- `local-ai`
- `license`
- `safety`
- `eval-candidate`
- `needs-review`

## 3. Convert To Eval

If the issue is safe and actionable:

```powershell
python scripts\add_feedback_eval.py --id community_NNN_short_name --query "sanitized question" --route product_search --required "expected text"
```

## 4. Verify

Run:

```powershell
$env:PYTHONDONTWRITEBYTECODE='1'
python scripts\scan_public_safety.py
python scripts\scan_license_safety.py
python scripts\run_eval.py
```

## 5. Decide

- If tests fail: fix lab behavior, then rerun.
- If tests pass: mark as covered.
- If feedback is unsafe or not relevant: close with explanation.

## 6. Private Transfer

Do not directly copy public feedback into the private company AI.

Use:

```text
public issue
-> sanitized eval
-> lab fix
-> private review
-> private AEOS gate
-> human approval
```
