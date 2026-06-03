# Public Feedback Plan

This lab exists to collect safe feedback without exposing the private company system.

## What We Want Feedback On

1. Wrong answer behavior.
2. Missing follow-up questions.
3. Confusing answer format.
4. OCR/table extraction ideas.
5. Lightweight local AI runtime ideas.
6. License or security concerns.
7. Better evaluation questions.

## What We Do Not Want

- Real customer documents.
- Real ERP screenshots.
- Real company price tables.
- Private logs.
- Private model files.
- Unreviewed copied code.

## Feedback Flow

```text
Public user opens issue
-> Maintainer checks for private data
-> If safe, classify issue
-> Add or update sample eval
-> Improve lab behavior
-> Run eval and safety scan
-> If useful, consider private system adaptation
```

## How Feedback Helps The Private AI

Public feedback should not directly change the private production AI.

Instead:

```text
Public feedback
-> public lab eval
-> safe pattern discovered
-> maintainer review
-> private implementation
-> private AEOS gate
-> human approval
```

## Simple Rule

The public lab teaches us better patterns.

The private system decides whether those patterns are safe enough for real company data.
