# 📖 Glossaire de l'IA agentique

Un glossaire de référence à consulter tout au long du parcours.

| Terme | Définition courte |
|-------|-------------------|
| **LLM** (Large Language Model) | Modèle de langage entraîné sur d'énormes corpus, capable de prédire le prochain token. Ex : GPT-4, Claude, Llama. |
| **Token** | Unité de base traitée par un LLM (≈ 0,75 mot en anglais, souvent moins en français). La facturation se fait au token. |
| **Context window** (fenêtre de contexte) | Quantité maximale de tokens que le modèle peut « voir » en une fois (prompt + réponse). Ex : 200k tokens. |
| **Embedding** | Représentation vectorielle d'un texte, permettant de mesurer la similarité sémantique. Base du RAG. |
| **Prompt** | Instruction/texte envoyé au modèle. |
| **System prompt** | Instruction de haut niveau qui définit le rôle et le comportement de l'agent. |
| **Température** | Paramètre (0–2) contrôlant l'aléatoire des réponses. Bas = déterministe, haut = créatif. |
| **Top-p** (nucleus sampling) | Alternative à la température : ne considère que les tokens dont la proba cumulée atteint p. |
| **Zero-shot / Few-shot** | Prompter sans exemple / avec quelques exemples pour guider le modèle. |
| **Chain-of-Thought (CoT)** | Inciter le modèle à raisonner étape par étape avant de répondre. |
| **Agent** | Système où un LLM décide **quelles actions entreprendre** (via des tools) en boucle, pour atteindre un objectif. |
| **Tool / Function calling** | Capacité d'un LLM à appeler des fonctions/outils externes (API, code, recherche...). |
| **ReAct** | Pattern *Reasoning + Acting* : le modèle alterne raisonnement et actions. |
| **Boucle agentique** | Cycle perception → raisonnement → action → observation, répété jusqu'à l'objectif. |
| **Mémoire** | Stockage d'informations entre les étapes/conversations (court terme = contexte, long terme = base externe). |
| **RAG** (Retrieval Augmented Generation) | Récupérer des documents pertinents et les injecter dans le contexte avant de générer. |
| **Sous-agent** | Agent spécialisé invoqué par un agent superviseur pour une sous-tâche. |
| **Orchestration multi-agents** | Coordination de plusieurs agents (superviseur/workers, pipeline, débat...). |
| **MCP** (Model Context Protocol) | Protocole ouvert standardisant la connexion des LLM à des sources de données et outils. |
| **Serveur MCP** | Programme exposant des *resources*, *tools* et *prompts* à un client compatible MCP. |
| **Skill / Custom agent** | Agent préconfiguré (rôle, instructions, outils) réutilisable et partageable. |
| **Coding agent** | Agent capable de modifier du code et d'ouvrir des pull requests de façon autonome. |
| **Eval** | Procédure d'évaluation mesurant la qualité/fiabilité des réponses d'un agent. |
| **Human-in-the-loop** | Point de validation humaine dans le workflow d'un agent. |
| **Prompt injection** | Attaque où un input malveillant détourne les instructions de l'agent. |
| **Hallucination** | Réponse plausible mais fausse générée par un LLM. |
| **Prompt caching** | Mise en cache d'une partie du prompt pour réduire coûts et latence. |

> 💡 Ce glossaire s'enrichira au fil des modules.
