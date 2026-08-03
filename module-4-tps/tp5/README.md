# TP5 — Industrialiser & partager un agent

## 🎯 Objectifs d'apprentissage

- Emballer un agent en package Python minimal.
- Séparer code, configuration et CLI.
- Préparer un artefact partageable dans une équipe.

## ⏱️ Durée estimée

1 h 30 à 2 h.

## ✅ Prérequis

- Modules 1 à 3 compris.
- Bases de packaging Python.

---

## Énoncé

Tu dois transformer un prototype d'agent en **petit package Python** partageable en interne.
Le package doit permettre de générer une configuration d'agent via une CLI.

### Attendus

- un `pyproject.toml` minimal ;
- une structure `src/` ;
- une configuration via variables d'environnement ;
- une commande CLI `scaffold`.

---

## Code fourni

- starter dans [`starter/`](./starter/)
- corrigé dans [`corrige/`](./corrige/)

### Exécution du corrigé

```bash
python module-4-tps/tp5/corrige/src/agent_factory/cli.py scaffold --name reviewer
```

---

## ✅ Auto-évaluation

1. Pourquoi passer par un package plutôt qu'un simple script isolé ?
<details><summary>Réponse</summary>Pour versionner, distribuer, documenter et réutiliser plus facilement l'agent dans une équipe.</details>

2. Pourquoi lire la configuration depuis l'environnement ?
<details><summary>Réponse</summary>Pour éviter les secrets en dur et adapter le comportement selon les environnements.</details>

3. Quel est le rôle d'une CLI de scaffolding ?
<details><summary>Réponse</summary>Créer rapidement une base cohérente d'agent ou de configuration sans repartir de zéro.</details>

---

## ➡️ Suite

Reviens au [Module 5 — IA dans le cycle de vie logiciel](../../module-5-sdlc/README.md).

> 💡 **Pour aller plus loin sur le partage d'agents** : consulte le guide complet
> [Partager un agent avec son équipe](../../module-5-sdlc/partager-un-agent.md)
> qui couvre GitHub Copilot, Claude Code, skills isolées et guide pas à pas reproductible.
