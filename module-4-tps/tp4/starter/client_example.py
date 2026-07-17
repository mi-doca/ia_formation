from __future__ import annotations

import json
from pathlib import Path


def build_claude_config(server_path: Path) -> dict:
    raise NotImplementedError("À compléter pendant le TP")


if __name__ == "__main__":
    print(json.dumps(build_claude_config(Path(__file__).with_name("server.py")), indent=2))
