# Module 3 — Utilisation en CLI

## 🎯 Objectifs d'apprentissage

- Utiliser GitHub Copilot et Claude depuis le terminal.
- Comprendre quand le mode CLI est plus efficace que le chat IDE.
- Intégrer des appels IA dans des scripts et workflows de dev.

## ⏱️ Durée estimée

1 h 30 à 2 h.

## ✅ Prérequis

- Avoir parcouru les modules 0 à 2.
- Être à l'aise avec les commandes shell de base.

---

## 1. Pourquoi la CLI est utile

Le terminal est idéal pour :

- automatiser des tâches répétitives ;
- chaîner des commandes ;
- travailler au plus près du dépôt et des logs ;
- intégrer l'IA dans des scripts, jobs CI ou aliases.

### Analogie

Le chat dans l'IDE est pratique pour discuter.
La **CLI** est pratique pour **produire un workflow reproductible**.

---

## 2. `gh copilot`

Selon ton installation GitHub CLI, tu peux disposer de commandes comme :

- `gh copilot suggest`
- `gh copilot explain`

### Exemples

```bash
gh copilot suggest "commande git pour annuler le dernier commit local sans perdre les fichiers"
gh copilot explain "git rebase --interactive HEAD~4"
```

### Cas d'usage utiles

- traduire une intention en commande shell ;
- expliquer une commande existante ;
- accélérer un diagnostic local.

### Bonnes pratiques

- relis toujours la commande proposée ;
- exécute-la d'abord sur un cas sans risque ;
- demande explicitement les hypothèses et effets de bord.

---

## 3. Claude Code en CLI

Selon la version, la commande peut être `claude` ou `claude-code`.
Vérifie systématiquement avec `--help`.

### Exemples conceptuels

```bash
claude --help
claude "résume les changements de ce dépôt"
claude "propose un plan de tests pour ce bug"
```

### Workflow typique

1. tu formules l'objectif ;
2. l'agent inspecte le dépôt ;
3. il planifie ;
4. il agit dans le cadre des permissions ;
5. tu relis, valides, corriges.

---

## 4. Automatiser des tâches de dev

### Exemple : enrichir un script shell existant

```bash
#!/usr/bin/env bash
set -euo pipefail

QUESTION="${1:-résume les changements récents du dépôt}"
gh copilot explain "$QUESTION"
```

### Exemple Python pilotant un CLI

```python
import subprocess


def run_command(command: list[str]) -> str:
    """Exécute une commande et retourne sa sortie texte."""
    result = subprocess.run(command, check=True, capture_output=True, text=True)
    return result.stdout.strip()


if __name__ == "__main__":
    print(run_command(["python", "--version"]))
```

---

## 5. Quand préférer la CLI au chat IDE ?

Choisis la CLI quand tu veux :

- lancer la même action plusieurs fois ;
- intégrer l'IA dans un pipeline ;
- travailler à partir d'un contexte terminal (logs, git, tests, scripts) ;
- garder une trace plus simple des commandes.

Garde le chat IDE quand tu veux :

- explorer du code visuellement ;
- itérer sur un design ;
- naviguer rapidement entre fichiers.

---

## 6. Exemples de prompts CLI efficaces

### Pour Copilot CLI

```text
Propose une commande Linux pour trouver les 20 fichiers Python les plus volumineux du dépôt.
```

### Pour Claude Code

```text
Analyse ce dossier Python et propose un plan en 5 étapes pour ajouter des tests sans toucher au code de prod.
```

### Variante plus robuste

```text
Contexte : dépôt Python orienté API.
Objectif : identifier les 3 zones les plus risquées.
Contraintes : réponse courte, structurée, citer les fichiers.
```

---

## 7. Risques fréquents en CLI

- donner trop de permissions ;
- lancer des commandes destructives sans relecture ;
- oublier que la sortie d'un tool peut contenir des secrets ou des données sensibles ;
- sur-automatiser un workflow pas encore stabilisé.

---

## ✅ Auto-évaluation

1. Pourquoi la CLI est-elle utile pour l'IA agentique ?
<details><summary>Réponse</summary>Parce qu'elle rend les workflows automatisables, reproductibles et faciles à intégrer dans des scripts ou pipelines.</details>

2. À quoi sert `gh copilot explain` ?
<details><summary>Réponse</summary>À expliquer une commande existante ou proposée, ce qui aide à comprendre ses effets de bord.</details>

3. Quand faut-il préférer la CLI au chat IDE ?
<details><summary>Réponse</summary>Quand on veut automatiser, enchaîner des commandes ou travailler directement depuis les logs, Git et les scripts.</details>

4. Pourquoi relire une commande suggérée par l'IA ?
<details><summary>Réponse</summary>Parce qu'une commande peut être destructive, inadaptée au contexte ou comporter des hypothèses implicites.</details>

5. Quelle est la bonne habitude avant d'utiliser une commande Claude Code ?
<details><summary>Réponse</summary>Vérifier la version et l'aide (`--help`) car les commandes exactes peuvent évoluer.</details>

---

## ➡️ Module suivant

Passe au [Module 4 — TPs pratiques](../module-4-tps/README.md).
