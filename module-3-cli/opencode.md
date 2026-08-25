# OpenCode — Agent CLI pour coder avec l'IA

## Qu'est-ce qu'OpenCode ?

**OpenCode** est un agent CLI open source qui te permet de piloter un LLM directement depuis ton terminal pour travailler sur un dépôt de code : explorer, modifier des fichiers, lancer des tests, générer des correctifs.

Contrairement à Copilot (intégré à l'IDE) ou Claude Code (produit Anthropic), OpenCode est :

- **open source** et configurable,
- **agnostique** au LLM (compatible OpenAI, Anthropic, Ollama, etc.),
- conçu pour fonctionner **dans le terminal**, au plus près du dépôt.

---

## Cas d'usage typiques

| Cas | Exemple |
|-----|---------|
| Explorer une codebase inconnue | « Explique-moi l'architecture de ce dépôt » |
| Générer ou modifier du code | « Ajoute une fonction de validation d'email dans `utils.py` » |
| Écrire ou améliorer des tests | « Génère des tests unitaires pour la fonction `parse_config` » |
| Appliquer un correctif | « Corrige le bug décrit dans ce traceback » |
| Refactoring ciblé | « Remplace toutes les f-strings par `.format()` dans `src/` » |
| Navigation dans un repo | « Quels fichiers gèrent la gestion des utilisateurs ? » |

---

## Installation rapide

```bash
# Via npm (méthode recommandée)
npm install -g opencode-ai

# Vérifier la version
opencode --version

# Aide
opencode --help
```

> **Note** : vérifie toujours la commande exacte sur la [doc officielle](https://opencode.ai/docs) car les CLI évoluent vite.

---

## Configuration minimale (exemple sans secrets)

Crée un fichier `opencode.json` à la racine du projet ou dans `~/.config/opencode/` :

```json
{
  "model": "claude-sonnet-4-5",
  "provider": "anthropic"
}
```

Les clés API sont à passer via des **variables d'environnement** (jamais en dur dans le fichier) :

```bash
export ANTHROPIC_API_KEY="ta-clé-api"
```

---

## Workflow pas à pas

### Étape 1 — Lancer OpenCode sur ton dépôt

```bash
cd mon-projet/
opencode
```

OpenCode ouvre une session interactive dans le terminal, avec accès au contenu du dépôt.

### Étape 2 — Poser une question sur le code

```
> Explique l'architecture générale de ce projet
```

OpenCode lit les fichiers du dépôt et génère une réponse contextuelle.

### Étape 3 — Lui demander de modifier un fichier

```
> Ajoute un paramètre `timeout` à la fonction `fetch_data` dans src/api.py
```

OpenCode propose une modification avec un diff.

### Étape 4 — Vérifier le diff avant d'accepter

```bash
git diff src/api.py
```

Relis toujours la modification avant de l'accepter ou de la committer.

### Étape 5 — Lancer les tests

```bash
pytest tests/
```

Vérifie que la modification n'a rien cassé.

### Étape 6 — Committer si tout va bien

```bash
git add src/api.py
git commit -m "feat: add timeout parameter to fetch_data"
```

---

## Tableau comparatif — OpenCode vs Copilot vs Claude Code

| Critère | GitHub Copilot | Claude Code | OpenCode |
|---------|---------------|-------------|----------|
| **Intégration** | IDE (VS Code, JetBrains, etc.) | Terminal / CLI | Terminal / CLI |
| **Source** | Propriétaire (Microsoft) | Propriétaire (Anthropic) | Open source |
| **Modèle** | GPT-4o / Copilot models | Claude (Anthropic) | Configurable (OpenAI, Anthropic, Ollama…) |
| **Contexte dépôt** | Via extensions agent | Oui, analyse le dépôt | Oui, analyse le dépôt |
| **Autonomie agent** | Chat + suggestions inline | Agent autonome avec tools | Agent autonome avec tools |
| **Coût** | Abonnement GitHub | API Anthropic (pay-as-you-go) | Selon le provider choisi |
| **Configuration** | Fichier `.instructions.md` | Fichier `CLAUDE.md` | Fichier `opencode.json` |
| **Idéal pour** | Autocomplétion + chat IDE | Workflows complexes en CLI | Flexibilité / sans lock-in |

### Quand utiliser quoi ?

- **Copilot** : tu codes dans l'IDE et veux de l'autocomplétion + un chat rapide.
- **Claude Code** : tu veux un agent autonome puissant pour des tâches complexes (refactor complet, exploration, debug long).
- **OpenCode** : tu veux un agent CLI open source, configurable, sans lock-in à un seul fournisseur.

---

## Bonnes pratiques

- Relis **toujours** le diff avant d'accepter une modification.
- Ne committe pas directement ce qu'OpenCode génère sans relecture.
- Garde les clés API dans des variables d'environnement, jamais dans les fichiers de config versionnés.
- Commence par des tâches ciblées (un fichier, une fonction) avant de lancer des refactors larges.
- Lis la sortie complète : OpenCode peut parfois faire des hypothèses implicites.

---

## ✅ Auto-évaluation

1. En quoi OpenCode diffère-t-il de GitHub Copilot ?
<details><summary>Réponse</summary>Copilot est intégré à l'IDE et propriétaire ; OpenCode est un agent CLI open source, agnostique au LLM.</details>

2. Quelle est la première chose à faire après qu'OpenCode modifie un fichier ?
<details><summary>Réponse</summary>Vérifier le diff avec `git diff` et relire la modification avant de l'accepter.</details>

3. Où placer sa clé API pour utiliser OpenCode de façon sécurisée ?
<details><summary>Réponse</summary>Dans une variable d'environnement (`export ANTHROPIC_API_KEY=...`), jamais en dur dans le fichier de config.</details>

---

## ➡️ Retour au module CLI

[← Retour au Module 3 — Utilisation en CLI](./README.md)
