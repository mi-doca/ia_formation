from __future__ import annotations

import json
from pathlib import Path



def build_claude_config(server_path: Path) -> dict:
    """Construit un exemple de configuration client MCP."""
    return {
        "mcpServers": {
            "release-notes": {
                "command": "python",
                "args": [str(server_path.resolve())],
            }
        }
    }


if __name__ == "__main__":
    print(json.dumps(build_claude_config(Path(__file__).with_name("server.py")), indent=2))
