from __future__ import annotations

import os
from dataclasses import dataclass


@dataclass
class AgentConfig:
    """Configuration minimale lue depuis l'environnement."""

    provider: str = os.getenv("AGENT_PROVIDER", "anthropic")
    model: str = os.getenv("AGENT_MODEL", "claude-sonnet")



def load_config() -> AgentConfig:
    return AgentConfig()
