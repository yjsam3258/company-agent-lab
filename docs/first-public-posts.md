# First Public Posts

Use these drafts after publishing the lab repository.

## 1. First Pinned Discussion

Title:

```text
How to give safe feedback
```

Body:

```text
Welcome to Company Agent Lab.

This is a public-safe playground for improving a local company assistant AI.

Please do not upload real company data:

- No real ERP screenshots.
- No real customer names.
- No phone numbers.
- No addresses.
- No real PDFs.
- No API keys.
- No private model files.

Good feedback examples:

- "This sample question should ask a follow-up question."
- "This OCR sample matched the wrong model and price."
- "This local AI runtime may be useful and has an MIT/Apache license."
- "This answer looks too confident without evidence."

Unsafe feedback examples:

- Real delivery documents.
- Real customer PDFs.
- Real company price tables.
- Screenshots containing private information.

How feedback becomes an improvement:

public feedback
-> safety review
-> sample eval
-> lab fix
-> private review
-> private AEOS gate
-> human approval

Thank you for helping improve the lab safely.
```

## 2. First Sample Issue

Issue template:

```text
Wrong answer report
```

Title:

```text
[Wrong Answer]: unclear stock question should still find 10W inventory
```

Question:

```text
10 watt stock available?
```

Actual answer:

```text
The lab may fail to understand "10 watt" if it only expects "10W".
```

Expected answer:

```text
It should find LUM-SAMPLE-010W-A and show current stock 8.
```

Problem type:

```text
Wrong product match
```

Maintainer action:

```powershell
python scripts\add_feedback_eval.py --id community_001_10w_text_stock --query "10 watt stock available?" --route product_search --required "LUM-SAMPLE-010W-A" --required "current stock 8"
python scripts\run_eval.py
```

## 3. First Maintainer Comment

```text
Thanks. This is safe sample feedback, so I marked it as eval-candidate.

I will add it as a regression test first. If the test fails, we will improve the lab behavior. If it passes, we keep it as a protection against future regressions.
```

## 4. Korean Summary For Internal Use

```text
이 공개 저장소는 회사 본체가 아니라 안전한 실험판입니다.

외부 피드백은 바로 본체 AI에 들어가지 않습니다.

먼저 공개 실험판에서:
1. 민감정보가 없는지 확인
2. 샘플 eval로 변환
3. 테스트 통과 확인
4. 좋은 방식만 비공개 본체에 별도로 검토

이 순서로만 반영합니다.
```
