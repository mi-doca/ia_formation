from __future__ import annotations

import argparse



def main() -> None:
    parser = argparse.ArgumentParser(description="TP packaging d'agent")
    parser.add_argument("command", choices=["scaffold"])
    parser.add_argument("--name", required=True)
    args = parser.parse_args()
    raise NotImplementedError(f"Compléter la commande {args.command} pour {args.name}")


if __name__ == "__main__":
    main()
