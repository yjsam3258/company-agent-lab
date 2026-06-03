from __future__ import annotations

import json
import re
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]

SAFE_LICENSES = {
    "MIT",
    "Apache-2.0",
    "BSD-2-Clause",
    "BSD-3-Clause",
}

BLOCKED_MARKERS = {
    "GPL",
    "AGPL",
    "LGPL",
    "CC-BY-SA",
    "NonCommercial",
    "Research Only",
    "No License",
    "Unknown",
}

MODEL_SUFFIXES = {".gguf", ".safetensors", ".bin", ".onnx", ".pt", ".pth"}
REQUIREMENT_FILES = ["requirements.txt", "requirements-dev.txt", "pyproject.toml", "package.json"]


def _scan_text_files() -> list[str]:
    failures: list[str] = []
    for path in ROOT.rglob("*"):
        if ".git" in path.parts or path.is_dir():
            continue
        rel = path.relative_to(ROOT)
        if path.suffix.lower() in MODEL_SUFFIXES:
            failures.append(f"model/binary weight file is not allowed in public lab: {rel}")
        if path.name in REQUIREMENT_FILES:
            text = path.read_text(encoding="utf-8", errors="ignore")
            for marker in BLOCKED_MARKERS:
                if re.search(re.escape(marker), text, re.IGNORECASE):
                    failures.append(f"blocked license marker in {rel}: {marker}")
    return failures


def _scan_intake_manifest() -> list[str]:
    manifest = ROOT / "docs" / "dependency-intake.json"
    if not manifest.exists():
        return []
    rows = json.loads(manifest.read_text(encoding="utf-8"))
    failures: list[str] = []
    for row in rows:
        name = str(row.get("name") or "")
        license_name = str(row.get("license") or "Unknown")
        if license_name not in SAFE_LICENSES:
            failures.append(f"dependency needs review or is blocked: {name} ({license_name})")
    return failures


def main() -> int:
    failures = _scan_text_files() + _scan_intake_manifest()
    if failures:
        print("License safety scan failed:")
        for failure in failures:
            print(f"- {failure}")
        return 1
    print("License safety scan passed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
