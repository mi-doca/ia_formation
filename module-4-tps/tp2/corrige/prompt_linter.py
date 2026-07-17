from __future__ import annotations

import sys
from pathlib import Path

REQUIRED_SECTIONS = ["objectif", "entrées", "sortie", "sécurité", "checklist"]


def read_markdown_files(base_dir: Path) -> list[Path]:
    """Retourne tous les fichiers Markdown à vérifier."""
    return sorted(base_dir.rglob("*.md"))



def validate_file(path: Path) -> list[str]:
    """Retourne la liste des sections manquantes pour un fichier donné."""
    content = path.read_text(encoding="utf-8").lower()
    return [section for section in REQUIRED_SECTIONS if section not in content]


if __name__ == "__main__":
    base_dir = Path(sys.argv[1]) if len(sys.argv) > 1 else Path(".")
    has_errors = False
    for path in read_markdown_files(base_dir):
        missing = validate_file(path)
        if missing:
            has_errors = True
            print(f"❌ {path}: sections manquantes -> {', '.join(missing)}")
        else:
            print(f"✅ {path}: structure OK")
    raise SystemExit(1 if has_errors else 0)
