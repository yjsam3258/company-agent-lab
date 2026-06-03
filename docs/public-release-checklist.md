# Public Release Checklist

Use this checklist before pushing the lab repository to GitHub.

## Data Safety

- [ ] No real ERP records.
- [ ] No real customer names.
- [ ] No real phone numbers.
- [ ] No real addresses.
- [ ] No real PDF files.
- [ ] No real OCR reports.
- [ ] No `outputs/`, `logs/`, or `audit/` folders.
- [ ] No `.env` files.
- [ ] No API keys or tokens.
- [ ] No private model weights.

## Legal Safety

- [ ] LICENSE exists.
- [ ] NOTICE exists.
- [ ] Third-party licenses are listed if dependencies are added.
- [ ] Model licenses are checked separately.
- [ ] No GPL/AGPL/CC-BY-SA/non-commercial dependency is included.

## Community Safety

- [ ] SECURITY.md exists.
- [ ] CONTRIBUTING.md exists.
- [ ] Issue templates warn users not to upload private data.
- [ ] README clearly says this is a public-safe lab, not the private company system.

## Quality Safety

- [ ] `python scripts\run_eval.py` passes.
- [ ] `python scripts\scan_public_safety.py` passes.
- [ ] Unknown facts trigger follow-up questions instead of fake answers.
