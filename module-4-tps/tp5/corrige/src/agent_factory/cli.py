from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

if __package__ in {None, ""}:
    sys.path.append(str(Path(__file__).resolve().parents[1]))
    from agent_factory.config import load_config
else:
    from agent_factory.config import load_config



def scaffold(name: str) -> dict:
    """Construit une base de configuration partageable pour un agent."""
    config = load_config()
    return {
        "name": name,
        "provider": config.provider,
        "model": config.model,
        "instructions": [
            "Décrire l'objectif",
            "Lister les tools autorisés",
            "Définir les garde-fous sécurité",
        ],
    }



def main() -> None:
    parser = argparse.ArgumentParser(description="Scaffold d'agent partageable")
    parser.add_argument("command", choices=["scaffold"])
    parser.add_argument("--name", required=True)
    args = parser.parse_args()

    if args.command == "scaffold":
        print(json.dumps(scaffold(args.name), ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
