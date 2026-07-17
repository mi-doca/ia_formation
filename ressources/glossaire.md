# 📖 Glossaire de l'IA agentique

Un glossaire de référence à consulter tout au long du parcours.

| Terme | Définition courte |
|-------|-------------------|
| **LLM** (Large Language Model) | Modèle de langage entraîné sur d'énormes corpus, capable de prédire le prochain token. Ex : GPT-4, Claude, Llama. |
| **Token** | Unité de base traitée par un LLM (≈ 0,75 mot en anglais). La facturation se fait au token. |
| **Context window** | Quantité maximale de tokens que le modèle peut voir en une fois (prompt + réponse). |
| **Embedding** | Représentation vectorielle d'un texte, permettant de mesurer la similarité sémantique. Base du RAG. |
| **Prompt** | Instruction/texte envoyé au modèle. |
| **System prompt** | Instruction de haut niveau définissant le rôle et le comportement de l'agent. |
| **Température** | Paramètre (0–2) contrôlant l'aléatoire des réponses. |
| **Top-p** | Alternative à la température (nucleus sampling). |
| **Zero-shot / Few-shot** | Prompter sans / avec quelques exemples. |
| **Chain-of-Thought (CoT)** | Inciter le modèle à raisonner étape par étape. |
| **Agent** | Système où un LLM décide quelles actions entreprendre (via des tools) en boucle. |
| **Tool / Function calling** | Capacité d'un LLM à appeler des fonctions/outils externes. |
| **ReAct** | Pattern Reasoning + Acting : alternance raisonnement/action. |
| **Boucle agentique** | Cycle perception → raisonnement → action → observation. |
| **Mémoire** | Stockage d'informations entre étapes (court terme = contexte, long terme = base externe). |
| **RAG** | Récupérer des documents pertinents et les injecter dans le contexte. |
| **Sous-agent** | Agent spécialisé invoqué par un agent superviseur. |
| **MCP** | Protocole ouvert standardisant la connexion des LLM aux données et outils. |
| **Serveur MCP** | Programme exposant resources, tools et prompts à un client MCP. |
| **Skill / Custom agent** | Agent préconfiguré réutilisable et partageable. |
| **Coding agent** | Agent capable de modifier du code et d'ouvrir des pull requests. |
| **Eval** | Procédure mesurant la qualité/fiabilité d'un agent. |
| **Human-in-the-loop** | Point de validation humaine dans le workflow. |
| **Prompt injection** | Attaque où un input malveillant détourne les instructions. |
| **Hallucination** | Réponse plausible mais fausse. |
| **Prompt caching** | Mise en cache d'une partie du prompt pour réduire coûts et latence. |

> 💡 Ce glossaire s'enrichit au fil des modules.
