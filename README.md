# 🎓 Parcours "Expert IA Agentique pour l'Ingénierie Logicielle"

Bienvenue dans ton parcours d'apprentissage complet pour maîtriser l'IA agentique
et l'appliquer concrètement au cycle de vie logiciel (tickets, développement, tests,
CI/CD, MCP).

> **Public visé** : développeur·se à l'aise en Python, débutant·e en IA agentique
> (utilisation en mode chat uniquement pour l'instant).
> **Outils pratiqués** : GitHub Copilot (chat, agent mode, coding agent, CLI) et Claude / Claude Code.

---

## 🧭 Comment suivre ce parcours

1. Suis les modules **dans l'ordre** (0 → 6). Chaque module a un `README.md` avec la théorie,
   des exemples, et des exercices.
2. Fais les **TPs** du Module 4 au fur et à mesure : ils sont progressifs.
3. À la fin de chaque module, tu trouveras une section **✅ Auto-évaluation** pour vérifier tes acquis.
4. Prends des notes dans le dossier `notes/`.

**Durée estimée** : 6 à 10 semaines à raison de quelques heures par semaine (adaptable).

---

## 📚 Sommaire des modules

| # | Module | Contenu | Statut |
|---|--------|---------|--------|
| 0 | [Fondations de l'IA générative](./module-0-fondations/) | LLM, tokens, contexte, tarification, prompting | ✅ Prêt |
| 1 | [Anatomie d'un agent](./module-1-agents/) | Boucle agentique, ReAct, tools, mémoire, RAG, sous-agents | ✅ Prêt |
| 2 | [Le protocole MCP](./module-2-mcp/) | Model Context Protocol, serveurs, clients, tools | ✅ Prêt |
| 3 | [Utilisation en CLI](./module-3-cli/) | `gh copilot`, Claude Code, automatisation terminal | ✅ Prêt |
| 4 | [TPs pratiques](./module-4-tps/) | Créer agents, skills, sous-agents, serveur MCP, industrialisation | ✅ Prêt |
| 5 | [IA dans le cycle logiciel](./module-5-sdlc/) | Tickets, dev, tests, CI/CD, MCP en production | ✅ Prêt |
| 6 | [Sujets avancés](./module-6-avance/) | Sécurité, evals, coûts, gouvernance, observabilité | ✅ Prêt |

---

## 🗺️ Vue d'ensemble des concepts couverts

### Fondations (les bases)
- Fonctionnement d'un LLM (tokens, embeddings, attention — niveau intuitif)
- Fenêtre de contexte, température, top-p
- **Tarification** : facturation input/output tokens, estimation de coûts
- Notion de **Plan** (raisonnement, décomposition de tâches)
- Techniques de prompting (zero-shot, few-shot, chain-of-thought)

### Agentique (le cœur)
- Différence LLM vs assistant vs **agent**
- La boucle agentique (ReAct)
- **Tools / Function calling**
- **Mémoire** et **RAG**
- **Sous-agents** et orchestration multi-agents
- **MCP** (Model Context Protocol)

### Pratique & industrialisation
- Utilisation en **CLI**
- Créer ses propres **agents / skills**
- Faire tourner des **sous-agents**
- **Industrialiser et partager** un agent

### Application à l'ingénierie logicielle
- Création automatisée de **tickets / issues**
- **Développement** assisté par agents
- Génération de **tests unitaires**
- **CI/CD** avec agents (GitHub Actions)
- Connexion aux outils internes via **MCP**

### Transverse
- **Sécurité** (prompt injection, secrets, permissions)
- **Évaluation** (evals) et fiabilité
- **Optimisation des coûts**
- **Gouvernance** (human-in-the-loop)
- **Observabilité** (tracing, logging)

---

## ✅ Prérequis techniques

- Python 3.10+
- Un compte GitHub avec accès à **GitHub Copilot**
- Un accès à **Claude** (web et/ou API Anthropic)
- Git et un IDE (VS Code recommandé)

---

## 📁 Structure du dépôt

```
ia_formation/
├���─ README.md                  ← tu es ici
├── module-0-fondations/
├── module-1-agents/
├── module-2-mcp/
├── module-3-cli/
├── module-4-tps/
├── module-5-sdlc/
├── module-6-avance/
├── notes/
└── ressources/
```

Bon apprentissage ! 🚀
