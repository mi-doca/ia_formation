"""
boucle_agentique.py
--------------------
Exemple minimal d'une boucle agentique avec function calling (API Anthropic).

Ce script reproduit exactement la mécanique décrite dans
``module-1-agents/fonctionnement-detaille.md`` :

- La liste de messages grossit à chaque tour.
- Le runtime (ce script) exécute les tools et ajoute le résultat au contexte.
- Le script logue la liste complète de messages avant chaque appel API
  pour que tu puisses *observer* le contexte s'accumuler.
- Une "correction" de l'utilisateur est simulée à la fin pour montrer
  comment elle influence la suite.

Prérequis
---------
    pip install anthropic

Configuration
-------------
    export ANTHROPIC_API_KEY="sk-ant-..."

Exécution
---------
    python module-1-agents/exemples/boucle_agentique.py
"""

from __future__ import annotations

import json
import os
from typing import Any

import anthropic

# ---------------------------------------------------------------------------
# Outils (tools) disponibles pour l'agent — implémentations mockées
# ---------------------------------------------------------------------------

# Contenu simulé d'un fichier de configuration
FAKE_FILES: dict[str, str] = {
    "config.py": (
        "# Configuration de l'application\n"
        "DB_HOST = 'localhost'\n"
        "DB_PORT = '5432'  # BUG : devrait être un int\n"
        "DB_NAME = 'mydb'\n"
        "DEBUG = True  # AVERTISSEMENT : à désactiver en production\n"
    )
}

# Résultats simulés des tests
FAKE_TEST_RESULTS = "2 tests passed. 0 failed."


def read_file(path: str) -> str:
    """Simule la lecture d'un fichier."""
    return FAKE_FILES.get(path, f"Erreur : fichier '{path}' introuvable.")


def write_file(path: str, content: str) -> str:
    """Simule l'écriture d'un fichier (en mémoire seulement pour la démo)."""
    FAKE_FILES[path] = content
    return f"Fichier '{path}' écrit avec succès ({len(content)} caractères)."


def run_tests() -> str:
    """Simule le lancement des tests."""
    return FAKE_TEST_RESULTS


# ---------------------------------------------------------------------------
# Définition des tools pour l'API Anthropic
# ---------------------------------------------------------------------------

TOOLS: list[dict[str, Any]] = [
    {
        "name": "read_file",
        "description": "Lit le contenu d'un fichier texte.",
        "input_schema": {
            "type": "object",
            "properties": {
                "path": {"type": "string", "description": "Chemin du fichier à lire."}
            },
            "required": ["path"],
        },
    },
    {
        "name": "write_file",
        "description": "Écrit du contenu dans un fichier texte.",
        "input_schema": {
            "type": "object",
            "properties": {
                "path": {"type": "string", "description": "Chemin du fichier à écrire."},
                "content": {
                    "type": "string",
                    "description": "Contenu complet à écrire dans le fichier.",
                },
            },
            "required": ["path", "content"],
        },
    },
    {
        "name": "run_tests",
        "description": "Lance les tests unitaires et renvoie le résumé.",
        "input_schema": {"type": "object", "properties": {}},
    },
]

# ---------------------------------------------------------------------------
# Fonctions utilitaires de logging
# ---------------------------------------------------------------------------

SEPARATOR = "─" * 60


def log_messages(messages: list[dict[str, Any]], tour: int) -> None:
    """Affiche la liste complète de messages avant chaque appel au modèle.

    C'est le cœur pédagogique : tu vois exactement ce que le modèle reçoit
    à chaque tour, et comment le contexte grandit.
    """
    print(f"\n{'═' * 60}")
    print(f"  Tour {tour} — Liste de messages envoyée au modèle")
    print(f"{'═' * 60}")
    print(f"  Nombre de messages : {len(messages)}")
    print(SEPARATOR)

    for i, msg in enumerate(messages):
        role = msg["role"].upper().ljust(10)
        content = msg["content"]

        if isinstance(content, str):
            # Message texte simple
            preview = content[:120].replace("\n", "↵")
            if len(content) > 120:
                preview += "…"
            print(f"  [{i}] {role}: {preview}")

        elif isinstance(content, list):
            # Message avec plusieurs blocs (assistant avec tool_use, ou tool_result)
            for block in content:
                btype = block.get("type", "?")
                if btype == "text":
                    preview = block["text"][:80].replace("\n", "↵")
                    print(f"  [{i}] {role}: [text] {preview}")
                elif btype == "tool_use":
                    print(
                        f"  [{i}] {role}: [tool_use] {block['name']}"
                        f"({json.dumps(block['input'], ensure_ascii=False)})"
                    )
                elif btype == "tool_result":
                    preview = str(block.get("content", ""))[:80].replace("\n", "↵")
                    print(
                        f"  [{i}] {role}: [tool_result id={block.get('tool_use_id', '?')[:8]}…]"
                        f" {preview}"
                    )
    print(SEPARATOR)


def execute_tool(name: str, inputs: dict[str, Any]) -> str:
    """Dispatche l'appel vers le bon tool et renvoie le résultat."""
    if name == "read_file":
        return read_file(inputs["path"])
    if name == "write_file":
        return write_file(inputs["path"], inputs["content"])
    if name == "run_tests":
        return run_tests()
    return f"Tool inconnu : {name}"


# ---------------------------------------------------------------------------
# Boucle agentique principale
# ---------------------------------------------------------------------------

SYSTEM_PROMPT = (
    "Tu es un agent de revue et correction de code Python. "
    "Tu peux lire des fichiers, écrire des fichiers corrigés et lancer des tests. "
    "Commence toujours par lire le fichier demandé avant de le modifier. "
    "Sois concis dans tes explications."
)


def run_agent(initial_message: str, max_turns: int = 10) -> None:
    """Lance la boucle agentique et logue le contexte à chaque tour.

    Args:
        initial_message: Demande initiale de l'utilisateur.
        max_turns: Nombre maximum d'itérations pour éviter les boucles infinies.
    """
    # Clé API lue depuis la variable d'environnement — jamais en dur !
    api_key = os.environ.get("ANTHROPIC_API_KEY")
    if not api_key:
        raise EnvironmentError(
            "Variable d'environnement ANTHROPIC_API_KEY non définie.\n"
            "  export ANTHROPIC_API_KEY='sk-ant-...'"
        )

    client = anthropic.Anthropic(api_key=api_key)

    # Liste de messages : c'est ici que tout se joue.
    # Elle grossit à chaque tour et est renvoyée EN ENTIER au modèle.
    messages: list[dict[str, Any]] = [
        {"role": "user", "content": initial_message}
    ]

    print(f"\n{'█' * 60}")
    print("  DÉMARRAGE DE LA BOUCLE AGENTIQUE")
    print(f"  Demande : {initial_message}")
    print(f"{'█' * 60}")

    tour = 1
    while tour <= max_turns:
        # ── Afficher la liste de messages avant l'appel ──────────────────────
        log_messages(messages, tour)

        # ── Appel API ─────────────────────────────────────────────────────────
        response = client.messages.create(
            model="claude-haiku-4-5",  # Haiku = moins cher pour tester
            max_tokens=1024,
            system=SYSTEM_PROMPT,
            tools=TOOLS,
            messages=messages,
        )

        print(f"\n  → stop_reason : {response.stop_reason}")

        # ── Ajouter la réponse du modèle à la liste de messages ───────────────
        # On stocke le contenu brut (liste de blocs) pour conserver les tool_use
        assistant_content = [block.model_dump() for block in response.content]
        messages.append({"role": "assistant", "content": assistant_content})

        # ── Si le modèle a terminé (pas de tool à exécuter) ───────────────────
        if response.stop_reason == "end_turn":
            # Récupérer le texte final
            final_text = " ".join(
                block.text
                for block in response.content
                if hasattr(block, "text")
            )
            print(f"\n{'═' * 60}")
            print("  RÉPONSE FINALE DE L'AGENT")
            print(f"{'═' * 60}")
            print(f"  {final_text}")
            print(SEPARATOR)
            break

        # ── Si le modèle veut appeler un ou plusieurs tools ───────────────────
        if response.stop_reason == "tool_use":
            tool_results = []

            for block in response.content:
                if block.type == "tool_use":
                    print(f"\n  ▶ Exécution tool : {block.name}({block.input})")
                    result = execute_tool(block.name, block.input)
                    print(f"    Résultat : {result[:120]}")

                    tool_results.append(
                        {
                            "type": "tool_result",
                            "tool_use_id": block.id,
                            "content": result,
                        }
                    )

            # Ajouter les résultats des tools au contexte (rôle "user" pour Anthropic)
            messages.append({"role": "user", "content": tool_results})
            tour += 1
        else:
            # stop_reason inattendu
            print(f"  stop_reason inattendu : {response.stop_reason}")
            break

    else:
        print(f"\n  ⚠ Nombre maximum de tours ({max_turns}) atteint.")


# ---------------------------------------------------------------------------
# Simulation d'une correction utilisateur en cours de session
# ---------------------------------------------------------------------------

def demo_correction_utilisateur() -> None:
    """Montre comment une correction de l'utilisateur influence la suite.

    La liste de messages accumule la correction et le modèle en tient compte
    dès le tour suivant — sans aucune magie, juste l'historique renvoyé.
    """
    api_key = os.environ.get("ANTHROPIC_API_KEY")
    if not api_key:
        raise EnvironmentError("ANTHROPIC_API_KEY non définie.")

    client = anthropic.Anthropic(api_key=api_key)

    print(f"\n\n{'█' * 60}")
    print("  DÉMO : CORRECTION UTILISATEUR EN COURS DE SESSION")
    print(f"{'█' * 60}")
    print(
        "\n  Cette démo montre comment une correction de l'utilisateur\n"
        "  est intégrée : elle s'ajoute simplement à la liste de messages\n"
        "  et le modèle la relit au prochain tour.\n"
    )

    # Étape 1 : demande initiale
    messages: list[dict[str, Any]] = [
        {"role": "user", "content": "Lis config.py et liste les problèmes que tu trouves."}
    ]

    log_messages(messages, 1)

    response = client.messages.create(
        model="claude-haiku-4-5",
        max_tokens=512,
        system=SYSTEM_PROMPT,
        tools=TOOLS,
        messages=messages,
    )

    # Simplification : on suppose que le modèle va appeler read_file
    assistant_content = [block.model_dump() for block in response.content]
    messages.append({"role": "assistant", "content": assistant_content})

    if response.stop_reason == "tool_use":
        tool_results = []
        for block in response.content:
            if block.type == "tool_use":
                result = execute_tool(block.name, block.input)
                tool_results.append(
                    {"type": "tool_result", "tool_use_id": block.id, "content": result}
                )
        messages.append({"role": "user", "content": tool_results})

        # Tour 2 : le modèle analyse et répond
        log_messages(messages, 2)
        response2 = client.messages.create(
            model="claude-haiku-4-5",
            max_tokens=512,
            system=SYSTEM_PROMPT,
            tools=TOOLS,
            messages=messages,
        )
        assistant_content2 = [block.model_dump() for block in response2.content]
        messages.append({"role": "assistant", "content": assistant_content2})

        analyse = " ".join(
            b.text for b in response2.content if hasattr(b, "text")
        )
        print(f"\n  Agent : {analyse[:200]}")

    # ─── Simulation de la correction utilisateur ─────────────────────────────
    correction = (
        "Attention, je veux que tu te concentres UNIQUEMENT sur les problèmes de sécurité, "
        "pas les conventions de style."
    )
    print(f"\n  Utilisateur (correction) : {correction}")

    # La correction s'ajoute à la liste — voilà tout le "secret"
    messages.append({"role": "user", "content": correction})

    log_messages(messages, 3)
    print("\n  → Le modèle relit tout l'historique + la correction.")
    print("     Il adaptera sa réponse en tenant compte de cette nouvelle contrainte.")

    response3 = client.messages.create(
        model="claude-haiku-4-5",
        max_tokens=512,
        system=SYSTEM_PROMPT,
        tools=TOOLS,
        messages=messages,
    )
    final = " ".join(b.text for b in response3.content if hasattr(b, "text"))
    print(f"\n  Agent (après correction) : {final[:300]}")
    print(SEPARATOR)
    print(
        "\n  Observation : le modèle a intégré la correction non pas parce qu'il\n"
        "  'apprend', mais parce qu'il a relu la liste de messages qui contient\n"
        "  maintenant ton instruction de correction.\n"
    )


# ---------------------------------------------------------------------------
# Point d'entrée
# ---------------------------------------------------------------------------

if __name__ == "__main__":
    # Démo principale : boucle agentique complète
    run_agent(
        initial_message=(
            "Lis le fichier config.py, identifie les problèmes, "
            "propose une version corrigée et lance les tests."
        )
    )

    # Démo secondaire : correction en cours de session
    demo_correction_utilisateur()
