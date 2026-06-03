# GitHub Publish Guide

This guide publishes the public-safe lab repository.

## 1. Create A New GitHub Repository

Go to GitHub and create a new repository:

```text
Repository name: company-agent-lab
Visibility: Public
Initialize with README: No
Add .gitignore: No
Choose a license: No
```

Why no README/license on GitHub?

This local folder already has:

- README.md
- LICENSE
- NOTICE
- SECURITY.md
- CONTRIBUTING.md

Creating extra files on GitHub can cause a first-push conflict.

## 2. Confirm Local Safety

Run:

```powershell
cd "C:\Users\yjsam\Desktop\AI 오픈소스\company-agent-lab"
$env:PYTHONDONTWRITEBYTECODE='1'
& "$env:USERPROFILE\.cache\codex-runtimes\codex-primary-runtime\dependencies\python\python.exe" scripts\scan_public_safety.py
& "$env:USERPROFILE\.cache\codex-runtimes\codex-primary-runtime\dependencies\python\python.exe" scripts\run_eval.py
```

Both must pass before pushing.

## 3. Push To GitHub

The remote is expected to be:

```text
https://github.com/yjsam3258/company-agent-lab.git
```

After creating the GitHub repository, run:

```powershell
cd "C:\Users\yjsam\Desktop\AI 오픈소스\company-agent-lab"
git push -u origin main
```

## 4. Turn On Feedback Channels

In GitHub repository settings:

- Enable Issues.
- Enable Discussions.
- Enable Dependabot alerts.
- Enable secret scanning if available.

## 5. First Pinned Discussion

Suggested title:

```text
How to give safe feedback
```

Suggested content:

```text
Please do not upload real company data, real PDFs, customer names, phone numbers, addresses, API keys, or private model files.

Use only sample data or sanitized examples.

Good feedback:
- "This sample question should ask a follow-up question."
- "This OCR sample pairs the wrong model and price."
- "This local runtime may be faster and has an MIT license."

Unsafe feedback:
- Real ERP screenshots.
- Real customer PDFs.
- Real delivery documents.
```

## 6. Private System Rule

Public feedback must not directly change the private company system.

Use this flow:

```text
public issue
-> safety review
-> sample eval
-> lab fix
-> private adaptation proposal
-> private AEOS gate
-> human approval
```
