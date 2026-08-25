# 🎓 Parcours "Expert en IA agentique pour l'ingénierie logicielle"

Bienvenue dans un parcours progressif, pratique et entièrement **en français** pour
passer d'un usage "chat dans l'IDE" à une vraie maîtrise de l'**IA agentique**
appliquée au développement logiciel.

> **Public visé** : développeur·se à l'aise en Python, débutant·e en IA agentique.  
> **Outils fil rouge** : GitHub Copilot, Claude / Claude Code, API Anthropic, un peu d'OpenAI pour comparer les approches.  
> **Philosophie** : comprendre les concepts, pratiquer vite, puis industrialiser.

---

## 🎯 Objectifs du parcours

À la fin de ce dépôt, tu sauras :

- expliquer clairement comment fonctionne un LLM sans entrer dans des maths lourdes ;
- distinguer **LLM**, **assistant**, **agent**, **tool**, **MCP**, **RAG** et **sous-agent** ;
- utiliser GitHub Copilot et Claude en mode **CLI**, **agent** et **API** ;
- concevoir des agents fiables pour coder, tester, documenter, créer des tickets et piloter des workflows ;
- raisonner en coût, sécurité, évaluation, gouvernance et observabilité.

---

## 🧭 Comment suivre ce parcours

1. Commence par le **Module 0** et avance dans l'ordre.
2. Fais les **TPs du Module 4** dès que tu termines les modules 1 à 3.
3. Utilise la section **✅ Auto-évaluation** à la fin de chaque module.
4. Garde le dossier [`notes/`](./notes/README.md) pour tes notes personnelles.
5. Reviens régulièrement au [`glossaire`](./ressources/glossaire.md) et à la [`cheatsheet prompting`](./ressources/cheatsheet-prompting.md).

**Durée indicative** : 6 à 10 semaines selon ton rythme et la profondeur de pratique.

📅 **Voir le [Plan de progression semaine par semaine](./PARCOURS.md)** — checklists de suivi incluses.

---

## ✅ Prérequis

- Python 3.10+
- Git et GitHub
- Un IDE avec GitHub Copilot
- Un accès à Claude (web, Desktop, CLI ou API Anthropic)
- Envie de pratiquer sur de vrais cas d'ingénierie logicielle

---

## 📚 Sommaire du parcours

| # | Module | Ce que tu y apprends |
|---|--------|----------------------|
| 0 | [Fondations de l'IA générative](./module-0-fondations/README.md) | Fonctionnement d'un LLM, tokens, embeddings, Transformer, contexte, tarification, plans, prompting |
| 1 | [Anatomie d'un agent](./module-1-agents/README.md) | Boucle agentique, ReAct, tools, mémoire, RAG, sous-agents — **+ [fonctionnement détaillé](./module-1-agents/fonctionnement-detaille.md)** |
| 2 | [Le protocole MCP](./module-2-mcp/README.md) | Architecture MCP, serveurs, clients, resources, prompts, tools |
| 3 | [Utilisation en CLI](./module-3-cli/README.md) | `gh copilot`, Claude Code, **[OpenCode](./module-3-cli/opencode.md)**, scripts et automatisation terminal |
| 4 | [TPs pratiques](./module-4-tps/README.md) | 5 ateliers complets avec code de départ et corrigés |
| 5 | [IA dans le cycle de vie logiciel](./module-5-sdlc/README.md) | Tickets, dev, tests, CI/CD, outillage interne — **+ [partager un agent](./module-5-sdlc/partager-un-agent.md)** |
| 6 | [Sujets avancés & bonnes pratiques](./module-6-avance/README.md) | Sécurité, evals, coûts, gouvernance, observabilité |

---

## 🛠️ Ressources transverses

- [`PARCOURS.md`](./PARCOURS.md) — plan de progression semaine par semaine avec checklists
- [`ressources/glossaire.md`](./ressources/glossaire.md)
- [`ressources/liens-utiles.md`](./ressources/liens-utiles.md)
- [`ressources/cheatsheet-prompting.md`](./ressources/cheatsheet-prompting.md)
- [`requirements.txt`](./requirements.txt) pour installer les dépendances utiles aux TPs

---

## 📁 Structure du dépôt

```text
ia_formation/
├── README.md
├── PARCOURS.md                               ← plan semaine par semaine avec checklists
├── module-0-fondations/README.md
├── module-1-agents/
│   ├── README.md
│   ├── fonctionnement-detaille.md        ← mémoire, trace d'un tour, idées reçues
│   └── exemples/boucle_agentique.py      ← code Python exécutable
├── module-2-mcp/README.md
├── module-3-cli/
│   ├── README.md
│   └── opencode.md                           ← intro, workflow pas à pas, comparatif CLI
├── module-4-tps/
│   ├── README.md
│   ├── tp1/
│   ├── tp2/
│   ├── tp3/
│   ├── tp4/
│   └── tp5/
├── module-5-sdlc/
│   ├── README.md
│   └── partager-un-agent.md              ← Copilot, Claude, skills, guide pas à pas
├── module-6-avance/README.md
├── ressources/
│   ├── glossaire.md
│   ├── liens-utiles.md
│   └── cheatsheet-prompting.md
├── requirements.txt
├── .gitignore
└── notes/README.md
```

---

## 🚀 Conseils pour bien progresser

- Lis les notions, puis **reformule-les avec tes mots**.
- Quand un concept te semble flou, crée un mini script Python pour le tester.
- Privilégie des agents **simples, traçables et testables** avant de viser des orchestrations complexes.
- Compare souvent : *ce que ferait un simple prompt* vs *ce qu'apporte réellement un agent*.

Bon apprentissage !
