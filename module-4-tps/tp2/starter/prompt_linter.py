from __future__ import annotations

import sys
from pathlib import Path

REQUIRED_SECTIONS = ["objectif", "entrées", "sortie", "sécurité", "checklist"]


def read_markdown_files(base_dir: Path) -> list[Path]:
    return list(base_dir.rglob("*.md"))


def validate_file(path: Path) -> list[str]:
    content = path.read_text(encoding="utf-8").lower()
    return [section for section in REQUIRED_SECTIONS if section not in content]


if __name__ == "__main__":
    base_dir = Path(sys.argv[1]) if len(sys.argv) > 1 else Path(".")
    for path in read_markdown_files(base_dir):
        missing = validate_file(path)
        print(f"{path}: manquants -> {missing}")
