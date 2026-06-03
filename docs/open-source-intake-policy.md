# Open Source Intake Policy

This project can learn from open source, but it must not copy risky code or ship unclear licenses.

## Preferred Licenses

These are allowed for lab experiments:

- MIT
- Apache-2.0
- BSD-2-Clause
- BSD-3-Clause

## Blocked Until Review

Do not add these without explicit review:

- GPL
- AGPL
- LGPL with unclear linking obligations
- CC-BY-SA
- Non-commercial licenses
- Research-only licenses
- Unknown license
- No license

## Safe Research Method

Allowed:

- Link to a repository.
- Explain an idea in your own words.
- Reimplement a pattern cleanly.
- Add a dependency only after license review.

Not allowed:

- Copy code from random repositories without checking the license.
- Add model weights without checking the model card and license.
- Upload private company data to test a public tool.

## Current Safe Runtime Candidates

These are candidates for research, not automatic dependencies:

- llama.cpp: lightweight local inference, MIT-style license.
- Ollama: easy local model runner, MIT.
- LocalAI: local OpenAI-compatible server, MIT.
- ONNX Runtime DirectML: Windows GPU route, useful for AMD GPU experiments.
- OpenVINO GenAI: CPU/Intel-oriented local inference, Apache-2.0.

Every model must be checked separately.

## Simple Rule

A safe tool plus an unsafe model is still unsafe.
