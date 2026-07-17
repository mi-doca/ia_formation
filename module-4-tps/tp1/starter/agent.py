from __future__ import annotations

from dataclasses import dataclass


@dataclass
class ToolCall:
    name: str
    arguments: dict


def add(a: int, b: int) -> int:
    """Retourne la somme de deux entiers."""
    raise NotImplementedError("À compléter pendant le TP")


def multiply(a: int, b: int) -> int:
    """Retourne le produit de deux entiers."""
    raise NotImplementedError("À compléter pendant le TP")


def get_mock_weather(city: str) -> dict:
    """Retourne une météo simplifiée pour quelques villes."""
    raise NotImplementedError("À compléter pendant le TP")


def plan_tool_calls(user_request: str) -> list[ToolCall]:
    """Détecte quels tools appeler à partir d'une requête simple."""
    raise NotImplementedError("À compléter pendant le TP")


def execute_tool_call(call: ToolCall):
    """Exécute un tool en fonction de son nom."""
    raise NotImplementedError("À compléter pendant le TP")


def build_final_answer(user_request: str, results: list[tuple[ToolCall, object]]) -> str:
    """Construit une synthèse lisible pour l'utilisateur."""
    raise NotImplementedError("À compléter pendant le TP")


if __name__ == "__main__":
    demo = "Calcule 6 * 7 et donne-moi la météo de Paris."
    calls = plan_tool_calls(demo)
    outputs = [(call, execute_tool_call(call)) for call in calls]
    print(build_final_answer(demo, outputs))
