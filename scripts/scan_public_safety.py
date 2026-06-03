from __future__ import annotations

import re
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]

FORBIDDEN_PATH_PARTS = {
    "outputs",
    "logs",
    "audit",
    "private",
    "real-data",
    "customer-data",
    "__pycache__",
}

FORBIDDEN_SUFFIXES = {
    ".pdf",
    ".png",
    ".jpg",
    ".jpeg",
    ".webp",
    ".bmp",
    ".tif",
    ".tiff",
    ".safetensors",
    ".bin",
    ".gguf",
    ".onnx",
}

SECRET_PATTERNS = {
    "openai_key": re.compile(r"sk-[A-Za-z0-9_-]{20,}"),
    "github_token": re.compile(r"(ghp_|github_pat_)[A-Za-z0-9_]{20,}"),
    "huggingface_token": re.compile(r"hf_[A-Za-z0-9]{20,}"),
    "assigned_secret": re.compile(r"(?i)(api[_-]?key|password|secret)\s*[:=]\s*['\"][^'\"]{8,}['\"]"),
    "phone_number": re.compile(r"01[016789][-\s]?\d{3,4}[-\s]?\d{4}"),
}

TEXT_SUFFIXES = {".py", ".md", ".json", ".yml", ".yaml", ".txt", ".gitignore"}


def main() -> int:
    failures: list[str] = []
    for path in ROOT.rglob("*"):
        if ".git" in path.parts:
            continue
        rel = path.relative_to(ROOT)
        if path.is_dir():
            continue
        if any(part in FORBIDDEN_PATH_PARTS for part in rel.parts):
            failures.append(f"forbidden path: {rel}")
        if path.suffix.lower() in FORBIDDEN_SUFFIXES:
            failures.append(f"forbidden file type: {rel}")
        if path.suffix.lower() not in TEXT_SUFFIXES and path.name not in {"LICENSE", "NOTICE"}:
            continue
        text = path.read_text(encoding="utf-8", errors="ignore")
        for name, pattern in SECRET_PATTERNS.items():
            if pattern.search(text):
                failures.append(f"possible private data or secret: {rel} ({name})")

    if failures:
        print("Public safety scan failed:")
        for failure in failures:
            print(f"- {failure}")
        return 1

    print("Public safety scan passed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
