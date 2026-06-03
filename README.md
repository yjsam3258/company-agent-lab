# Company Agent Lab

Company Agent Lab is a public-safe playground for improving a local business assistant AI.

This repository is **not** the private company production system. It contains only sample data, toy examples, public-safe evaluation scripts, and feedback templates.

## What This Project Tries To Improve

The goal is to make a small local AI assistant better at practical company tasks:

- Understand product search questions.
- Read safe sample product facts.
- Answer with evidence instead of guessing.
- Ask a follow-up question when the request is unclear.
- Learn from wrong answers through feedback.
- Keep private company data out of public code.

## What Is Safe To Share Here

Allowed:

- Fake ERP records.
- Fake product data.
- Fake PDF/OCR examples.
- Test questions and expected answers.
- Local AI connection examples.
- Evaluation rules.
- Bug reports without private data.

Not allowed:

- Real customer names.
- Real phone numbers, addresses, or emails.
- Real ERP exports.
- Real delivery request numbers.
- Real PDF files from customers or public institutions.
- API keys, tokens, passwords, cookies, or `.env` files.
- Private model adapters or unreviewed model weights.
- Company price tables unless explicitly sanitized.

## Simple Explanation

Think of this repository as a practice notebook.

The real company notebook stays private. This public notebook uses pretend data so other developers can safely point out mistakes and suggest improvements.

## Current Lab Features

- Rule-based sample answer engine.
- Safe fake product data.
- Safe fake ERP records.
- Small evaluation script.
- Public safety scanner.
- License safety scanner.
- GitHub issue templates for feedback.
- GitHub Actions safety CI.
- Security and contribution guidelines.

## Quick Start

```powershell
cd company-agent-lab
python scripts\answer.py "10W stock?"
python scripts\answer.py "warm white bollard"
python scripts\run_eval.py
python scripts\scan_public_safety.py
python scripts\scan_license_safety.py
```

## Feedback

Use GitHub Issues or Discussions:

- Wrong answer report.
- OCR extraction failure.
- Local model/runtime idea.
- License or security concern.
- Feature suggestion.

Please remove all private data before posting.

Start here:

- [How to give safe feedback](docs/first-public-posts.md)
- [Feedback management](docs/feedback-management.md)
- [Public release checklist](docs/public-release-checklist.md)

Korean summary:

```text
이 공개 저장소는 회사 본체가 아니라 안전한 실험판입니다.
실제 ERP 데이터, 실제 PDF, 고객정보, API 키, 비공개 모델 파일은 올리지 마세요.
```

## Recommended Local AI Research Direction

The safest first experiments are:

- `llama.cpp` for lightweight local inference.
- `Ollama` for easy local model running.
- `LocalAI` for OpenAI-compatible local API testing.
- Small permissive-license models only, such as MIT or Apache-2.0 candidates.

Every model must be reviewed separately. A safe runtime does not automatically make the model safe.

## Safety Rule

If a change improves answer quality but weakens privacy or legal safety, it should not be merged.

Good improvement:

```text
The assistant asks a better follow-up question when data is missing.
```

Bad improvement:

```text
The assistant accepts real ERP files in public issues.
```

## License

This lab repository is released under the MIT License.
