# 🗺️ Plan de progression suggéré

Ce planning indicatif sur **8 semaines** est conçu pour un rythme de 3 à 5 heures par semaine.
Adapte-le à ton rythme : le parcours reste valide si tu le fais en 6 ou en 10 semaines.

> **Comment utiliser ce fichier** : coche les cases au fur et à mesure (via une copie locale ou en créant ton propre fork du dépôt).

---

## Semaine 1 — Fondations et mise en place

**Objectif** : comprendre comment fonctionne un LLM, configurer l'environnement.

- [ ] Lire [Module 0 — Fondations](./module-0-fondations/README.md) en entier
- [ ] Relire la section "Du prompt à la réponse" et refaire mentalement l'exemple pas à pas sur `j'aimerai comprendre comment fonctionne un LLM`
- [ ] Faire les exercices de calcul de coût (sections 6.4 et 6.5)
- [ ] Installer Python 3.10+, Git et un IDE avec GitHub Copilot
- [ ] Créer un environnement virtuel et installer les dépendances : `pip install -r requirements.txt`
- [ ] Faire les exercices de prompting (section 8 du Module 0)
- [ ] Parcourir le [Glossaire](./ressources/glossaire.md) une première fois
- [ ] Consulter la [Cheatsheet prompting](./ressources/cheatsheet-prompting.md)

---

## Semaine 2 — Anatomie d'un agent

**Objectif** : comprendre la boucle agentique, les tools et la mémoire.

- [ ] Lire [Module 1 — Anatomie d'un agent](./module-1-agents/README.md)
- [ ] Lire [Fonctionnement détaillé d'un agent](./module-1-agents/fonctionnement-detaille.md)
  - [ ] Comprendre pourquoi un LLM stateless donne l'illusion de mémoire
  - [ ] Suivre la trace pas à pas d'un tour agentique complet
  - [ ] Relire les 5 idées reçues à déconstruire
- [ ] *(Optionnel)* Configurer `ANTHROPIC_API_KEY` et lancer `module-1-agents/exemples/boucle_agentique.py`
- [ ] Compléter l'auto-évaluation du Module 1

---

## Semaine 3 — MCP et CLI

**Objectif** : comprendre le protocole MCP et utiliser l'IA depuis le terminal.

- [ ] Lire [Module 2 — Le protocole MCP](./module-2-mcp/README.md)
  - [ ] Comprendre la différence tool / resource / prompt
  - [ ] Lire l'exemple de serveur MCP minimal
  - [ ] Compléter l'auto-évaluation du Module 2
- [ ] Lire [Module 3 — Utilisation en CLI](./module-3-cli/README.md)
  - [ ] Lire la section dédiée [OpenCode](./module-3-cli/opencode.md)
  - [ ] Tester `gh copilot suggest` et `gh copilot explain` avec un exemple réel
  - [ ] Tester OpenCode sur un dépôt : question, modification ciblée, vérification du diff puis des tests
  - [ ] Compléter l'auto-évaluation du Module 3

---

## Semaine 4 — TP1 et TP2 : premiers agents

**Objectif** : construire un premier agent et formaliser des skills.

- [ ] Lire [Module 4 — TPs pratiques](./module-4-tps/README.md) (introduction)
- [ ] Faire [TP1 — Premier agent](./module-4-tps/tp1/README.md)
  - [ ] Compléter le `starter/agent.py`
  - [ ] Comparer avec `corrige/agent.py`
  - [ ] Exécuter : `python module-4-tps/tp1/corrige/agent.py`
- [ ] Faire [TP2 — Skills / custom agents](./module-4-tps/tp2/README.md)
  - [ ] Rédiger le fichier d'instructions Copilot
  - [ ] Rédiger le skill Markdown pour Claude
  - [ ] Compléter et exécuter le validateur Python
  - [ ] Comparer avec le corrigé

---

## Semaine 5 — TP3 et TP4 : sous-agents et MCP

**Objectif** : orchestrer plusieurs agents et construire un vrai serveur MCP.

- [ ] Faire [TP3 — Orchestrer des sous-agents](./module-4-tps/tp3/README.md)
  - [ ] Compléter `starter/orchestrator.py`
  - [ ] Exécuter et comparer avec le corrigé
- [ ] Faire [TP4 — Serveur MCP custom](./module-4-tps/tp4/README.md)
  - [ ] Compléter `starter/server.py`
  - [ ] Compléter `starter/client_example.py`
  - [ ] Comparer avec le corrigé et exécuter : `python module-4-tps/tp4/corrige/client_example.py`

---

## Semaine 6 — TP5 et partage d'agents

**Objectif** : industrialiser un agent et apprendre à partager ses skills avec l'équipe.

- [ ] Faire [TP5 — Industrialiser & partager un agent](./module-4-tps/tp5/README.md)
  - [ ] Explorer la structure `src/agent_factory/`
  - [ ] Compléter le starter
  - [ ] Exécuter : `python module-4-tps/tp5/corrige/src/agent_factory/cli.py scaffold --name reviewer`
- [ ] Lire [Partager un agent avec son équipe](./module-5-sdlc/partager-un-agent.md)
  - [ ] Comprendre config personnelle vs partagée
  - [ ] Créer une structure `.github/` et `.claude/` sur un projet test
  - [ ] Suivre le guide pas à pas reproductible (section 5)

---

## Semaine 7 — IA dans le cycle de vie logiciel

**Objectif** : intégrer l'IA agentique dans le SDLC au quotidien.

- [ ] Lire [Module 5 — IA dans le SDLC](./module-5-sdlc/README.md)
  - [ ] Rédiger une vraie issue à partir d'un incident ou log réel
  - [ ] Tester la génération de tests unitaires sur une fonction de ton code
  - [ ] Identifier 2–3 points d'intégration CI/CD dans un projet existant
  - [ ] Compléter l'auto-évaluation du Module 5
- [ ] Consulter les [Liens utiles](./ressources/liens-utiles.md) pour approfondir

---

## Semaine 8 — Sujets avancés et consolidation

**Objectif** : maîtriser sécurité, evals, coûts, gouvernance ; consolider le parcours.

- [ ] Lire [Module 6 — Sujets avancés](./module-6-avance/README.md)
  - [ ] Identifier les risques de prompt injection dans un usage réel
  - [ ] Définir 10 cas d'évaluation pour un agent que tu as construit
  - [ ] Calculer le coût mensuel d'un agent hypothétique (adapte l'exercice du Module 0)
  - [ ] Remplir la check-list de mise en prod (section 6 du Module 6)
  - [ ] Compléter l'auto-évaluation du Module 6
- [ ] **Bilan personnel** :
  - [ ] Relire le [Glossaire](./ressources/glossaire.md) et vérifier que chaque terme est bien compris
  - [ ] Choisir un cas métier réel et concevoir un mini-agent (même sur papier)
  - [ ] Identifier la prochaine étape : serveur MCP interne, suite d'evals, déploiement CI/CD

---

## Récapitulatif rapide

| Semaine | Modules / TPs | Durée estimée |
|---------|---------------|---------------|
| 1 | Module 0 | 3 h – 4 h |
| 2 | Module 1 + fonctionnement détaillé | 3 h – 4 h |
| 3 | Modules 2 + 3 | 3 h – 5 h |
| 4 | TP1 + TP2 | 2 h – 3 h |
| 5 | TP3 + TP4 | 2 h – 4 h |
| 6 | TP5 + partager-un-agent | 3 h – 4 h |
| 7 | Module 5 | 3 h – 4 h |
| 8 | Module 6 + consolidation | 3 h – 4 h |
| **Total** | **7 modules + 5 TPs** | **22 h – 32 h** |

---

## 💡 Conseils pour tenir le rythme

- Fixe un créneau régulier dans ta semaine (même 45 min par jour suffit).
- Après chaque module, reformule les 3 idées principales avec tes propres mots.
- Utilise le dossier [`notes/`](./notes/README.md) pour noter tes questions et réalisations.
- Compare tes solutions de TP avant de regarder le corrigé.

---

*Bon parcours ! 🚀*
