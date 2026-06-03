# Contributing

Thank you for helping improve Company Agent Lab.

## Good Contributions

- Better sample questions.
- Better expected answers.
- Better follow-up question behavior.
- Safer PII redaction rules.
- Clearer evaluation tests.
- Local AI runtime experiments with clean licenses.
- Documentation that helps non-developers understand the system.

## Before Opening A Pull Request

Please check:

1. No private company data is included.
2. No API keys or `.env` files are included.
3. No real PDFs or screenshots are included.
4. Any new dependency has a clear license.
5. The evaluation script still passes.

Run:

```powershell
python scripts\run_eval.py
python scripts\scan_public_safety.py
```

## Dependency Rule

Preferred licenses:

- MIT
- Apache-2.0
- BSD-2-Clause
- BSD-3-Clause

Blocked unless explicitly reviewed:

- GPL
- AGPL
- LGPL with unclear linking
- CC-BY-SA
- Non-commercial
- Research-only
- Unknown or no license

## Answer Quality Rule

The assistant should not pretend to know missing facts.

Good:

```text
I found 2 candidates. The due date is not in the sample data. Which project should I check?
```

Bad:

```text
The due date is tomorrow.
```

when there is no evidence.
