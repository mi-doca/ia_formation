from __future__ import annotations

import re
from dataclasses import dataclass


@dataclass
class ToolCall:
    name: str
    arguments: dict


WEATHER_SAMPLES = {
    "paris": {"ville": "Paris", "temperature": 22, "condition": "ensoleillé"},
    "lyon": {"ville": "Lyon", "temperature": 19, "condition": "nuageux"},
    "marseille": {"ville": "Marseille", "temperature": 27, "condition": "venteux"},
}


def add(a: int, b: int) -> int:
    """Retourne la somme de deux entiers."""
    return a + b



def multiply(a: int, b: int) -> int:
    """Retourne le produit de deux entiers."""
    return a * b



def get_mock_weather(city: str) -> dict:
    """Retourne une météo simplifiée pour quelques villes."""
    return WEATHER_SAMPLES.get(city.lower(), {"ville": city, "temperature": 0, "condition": "inconnue"})



def plan_tool_calls(user_request: str) -> list[ToolCall]:
    """Détecte quels tools appeler à partir d'une requête simple."""
    lowered = user_request.lower()
    calls: list[ToolCall] = []

    addition_match = re.search(r"(\d+)\s*\+\s*(\d+)", lowered)
    multiplication_match = re.search(r"(\d+)\s*\*\s*(\d+)", lowered)

    if addition_match:
        calls.append(
            ToolCall(
                name="add",
                arguments={"a": int(addition_match.group(1)), "b": int(addition_match.group(2))},
            )
        )

    if multiplication_match:
        calls.append(
            ToolCall(
                name="multiply",
                arguments={"a": int(multiplication_match.group(1)), "b": int(multiplication_match.group(2))},
            )
        )

    for city in WEATHER_SAMPLES:
        if city in lowered:
            calls.append(ToolCall(name="get_mock_weather", arguments={"city": city}))

    return calls



def execute_tool_call(call: ToolCall):
    """Exécute un tool en fonction de son nom."""
    if call.name == "add":
        return add(**call.arguments)
    if call.name == "multiply":
        return multiply(**call.arguments)
    if call.name == "get_mock_weather":
        return get_mock_weather(**call.arguments)
    raise ValueError(f"Tool inconnu : {call.name}")



def build_final_answer(user_request: str, results: list[tuple[ToolCall, object]]) -> str:
    """Construit une synthèse lisible pour l'utilisateur."""
    lines = [f"Demande comprise : {user_request}", "Résultats :"]
    for call, result in results:
        if call.name in {"add", "multiply"}:
            lines.append(f"- {call.name}({call.arguments['a']}, {call.arguments['b']}) = {result}")
        elif call.name == "get_mock_weather":
            lines.append(
                f"- météo de {result['ville']} : {result['temperature']}°C, {result['condition']}"
            )
    return "\n".join(lines)


if __name__ == "__main__":
    demo = "Calcule 6 * 7 et donne-moi la météo de Paris."
    calls = plan_tool_calls(demo)
    outputs = [(call, execute_tool_call(call)) for call in calls]
    print(build_final_answer(demo, outputs))
