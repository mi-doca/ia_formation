# 📖 Glossaire de l'IA agentique

| Terme | Définition courte |
|-------|-------------------|
| **LLM** | Modèle de langage prédisant le prochain token. Ex : GPT-4, Claude. |
| **Token** | Unité de base traitée par un LLM (≈ 0,75 mot en anglais). Base de la facturation. |
| **Context window** | Nombre max de tokens visibles en une fois (prompt + réponse). |
| **Embedding** | Vecteur représentant un texte pour mesurer la similarité. Base du RAG. |
| **Prompt** | Texte envoyé au modèle. |
| **System prompt** | Instruction définissant le rôle/comportement de l'agent. |
| **Température** | Paramètre (0–2) contrôlant l'aléatoire. |
| **Top-p** | Nucleus sampling, alternative à la température. |
| **Zero/Few-shot** | Prompter sans / avec exemples. |
| **Chain-of-Thought** | Raisonner étape par étape. |
| **Agent** | LLM qui décide d'actions via des tools, en boucle. |
| **Tool / Function calling** | Appel de fonctions externes par le LLM. |
| **ReAct** | Pattern Reasoning + Acting. |
| **RAG** | Récupérer + injecter des documents dans le contexte. |
| **Sous-agent** | Agent spécialisé invoqué par un superviseur. |
| **MCP** | Protocole standard connectant LLM ↔ données/outils. |
| **Skill / Custom agent** | Agent préconfiguré réutilisable. |
| **Coding agent** | Agent modifiant du code et ouvrant des PR. |
| **Eval** | Évaluation de la qualité d'un agent. |
| **Human-in-the-loop** | Validation humaine dans le workflow. |
| **Prompt injection** | Attaque détournant les instructions. |
| **Hallucination** | Réponse plausible mais fausse. |
| **Prompt caching** | Cache d'une partie du prompt (coûts/latence). |
