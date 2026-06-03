# Local AI Roadmap

The lab should grow from a rule-based sample assistant into a test bench for small local AI models.

## Stage 1: Public-Safe Rule Baseline

Status: started.

Purpose:

- Make a tiny assistant that answers from fake data.
- Prove that evaluation and safety scanning work.
- Collect feedback without private data.

## Stage 2: Local Model Adapter

Goal:

- Add optional connectors for local model runtimes.

Candidates:

- Ollama.
- llama.cpp server.
- LocalAI.

Rule:

- Runtime license and model license must both be checked.
- Local model answers must be compared against the deterministic baseline.

## Stage 3: Better Question Understanding

Goal:

- Let a local model help interpret questions.

Example:

```text
"10W 재고 있는거 있나?"
-> intent: product_inventory_search
-> filters: power=10W, stock>0
```

The model may suggest intent, but the final answer must still be grounded in data.

## Stage 4: Feedback Learning

Goal:

- Turn wrong answer reports into new eval tasks.

Flow:

```text
wrong answer issue
-> sanitized task
-> expected answer
-> eval
-> fix
-> pass
```

## Stage 5: Private System Transfer

Goal:

- Move only safe, proven ideas into the private company AI.

Never transfer:

- Public user data without review.
- Unlicensed code.
- Unverified model weights.
- Any behavior that weakens privacy or factual grounding.

## Long-Term Direction

The AI should not become smarter by adding endless rigid rules.

It should improve by:

- Seeing more safe examples.
- Asking better follow-up questions.
- Testing itself.
- Separating guesses from evidence.
- Promoting only strategies that pass evaluation.
