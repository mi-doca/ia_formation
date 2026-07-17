# TP2 — Créer ses propres skills / custom agents

## 🎯 Objectifs d'apprentissage

- Formaliser des instructions réutilisables.
- Différencier une consigne floue d'une consigne opérationnelle.
- Vérifier automatiquement la présence de sections importantes.

## ⏱️ Durée estimée

45 min à 1 h.

## ✅ Prérequis

- Module 1 compris.
- Aisance avec Markdown et structure de prompts.

---

## Énoncé

Tu dois créer un **profil d'agent de revue de code Python** utilisable dans un environnement type Copilot ou Claude.

### Livrables

- un fichier d'instructions Copilot ;
- un skill Markdown pour Claude ;
- un mini validateur Python qui vérifie que certaines sections sont présentes.

### Sections attendues

- objectif ;
- entrées ;
- sortie attendue ;
- garde-fous sécurité ;
- checklist finale.

---

## Code fourni

- [`starter/.github/copilot-instructions.md`](./starter/.github/copilot-instructions.md)
- [`starter/claude/skill.md`](./starter/claude/skill.md)
- [`starter/prompt_linter.py`](./starter/prompt_linter.py)
- corrigé équivalent dans `corrige/`

### Exécution du corrigé

```bash
python module-4-tps/tp2/corrige/prompt_linter.py module-4-tps/tp2/corrige
```

---

## ✅ Auto-évaluation

1. Pourquoi écrire des instructions réutilisables ?
<details><summary>Réponse</summary>Pour cadrer durablement le comportement d'un agent et éviter de répéter les mêmes contraintes.</details>

2. Pourquoi ajouter un linter de prompt, même très simple ?
<details><summary>Réponse</summary>Pour détecter vite les oublis de sections critiques comme la sécurité ou le format de sortie.</details>

3. Quelle différence entre un prompt ad hoc et un skill ?
<details><summary>Réponse</summary>Le skill est pensé pour être réutilisé, maintenu et partagé dans plusieurs contextes.</details>

---

## ➡️ TP suivant

Passe au [TP3 — Orchestrer des sous-agents](../tp3/README.md).
