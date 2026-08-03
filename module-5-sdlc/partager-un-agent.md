# 🤝 Partager un agent avec son équipe

> **Objectif de cette section** : comprendre concrètement comment créer, versionner et
> partager un agent (avec toutes ses skills ou une seule skill) pour que tes coéquipiers
> puissent l'utiliser sans configuration supplémentaire.

---

## Sommaire

1. [Concepts clés : config personnelle vs config partagée](#1-concepts-clés)
2. [Partage via GitHub Copilot](#2-partage-via-github-copilot)
3. [Partage via Claude / Claude Code](#3-partage-via-claude--claude-code)
4. [Bonnes pratiques d'industrialisation](#4-bonnes-pratiques)
5. [Guide pas à pas reproductible](#5-guide-pas-à-pas)
6. [Auto-évaluation](#-auto-évaluation)

---

## 1. Concepts clés

### Config personnelle vs config partagée

| Type | Où ça vit | Qui en bénéficie | Comment partager |
|------|-----------|------------------|-----------------|
| **Personnelle** | `~/.config/`, `~/.claude/`, paramètres VS Code utilisateur | Toi seul | Tu ne peux pas (ou en dehors du repo) |
| **Partagée** | Dans le dépôt Git (`.github/`, `.claude/`, etc.) | Toute l'équipe qui clone le repo | `git commit` + `git push` |

> **Règle d'or** : tout ce que tu veux partager doit être **dans le repo Git**.
> Tout ce qui est personnel (clés API, préférences locales) doit rester **hors du repo**.

### Agent complet vs une seule skill

```text
Agent complet
└── .github/
│   └── copilot-instructions.md    ← persona + contexte global
└── .claude/
    ├── CLAUDE.md                  ← instructions Claude pour ce repo
    ├── agents/
    │   └── reviewer.md            ← sous-agent de revue
    └── skills/
        ├── lint-check.md          ← skill isolée #1
        └── test-generator.md      ← skill isolée #2

Partager UNE skill isolée
└── .claude/skills/test-generator.md  ← copie juste ce fichier dans un autre repo
```

---

## 2. Partage via GitHub Copilot

### 2.1 `.github/copilot-instructions.md` — instructions partagées automatiquement

Ce fichier est **lu automatiquement par GitHub Copilot** pour tous les membres de l'équipe
qui travaillent sur le repo. C'est le moyen le plus simple de partager un contexte commun.

**Emplacement :** `.github/copilot-instructions.md`

**Exemple de contenu :**

```markdown
# Instructions Copilot — MonProjet

## Contexte
Ce dépôt contient une API REST Python (FastAPI). Les tests utilisent pytest.
Le style de code suit PEP 8 et les types sont annotés partout.

## Conventions
- Nommage : snake_case pour les variables, PascalCase pour les classes.
- Toutes les fonctions publiques ont une docstring au format Google.
- Les secrets sont lus depuis les variables d'environnement (jamais en dur).

## Comportement attendu de Copilot
- Propose toujours des tests pytest avec le code.
- Signale les cas limites (None, liste vide, valeurs négatives).
- Ne modifie pas les fichiers hors du scope de la demande.
```

**Comment un coéquipier l'utilise :** il n'a rien à faire. Dès qu'il clone le repo et
ouvre VS Code avec Copilot, les instructions sont automatiquement appliquées.

### 2.2 Prompt files et instructions files

Ces fichiers permettent de définir des **agents spécialisés réutilisables** dans VS Code.

| Type de fichier | Extension | Rôle |
|----------------|-----------|------|
| **Prompt file** | `.prompt.md` | Définit un prompt réutilisable (slash command dans le chat) |
| **Instructions file** | `.instructions.md` | Instructions qui s'appliquent à un contexte de fichier |

**Emplacement recommandé dans le repo :**

```text
.github/
└── copilot/
    ├── prompts/
    │   ├── code-review.prompt.md
    │   └── test-generator.prompt.md
    └── instructions/
        ├── python.instructions.md
        └── api.instructions.md
```

**Exemple — `.github/copilot/prompts/code-review.prompt.md` :**

```markdown
---
mode: ask
description: Revue de code ciblée sur les risques
---

Analyse le code sélectionné et liste uniquement :
1. Les bugs potentiels (null pointer, division par zéro, etc.)
2. Les failles de sécurité (injection, secret exposé, etc.)
3. Les tests manquants pour les cas limites

Format de réponse : liste priorisée, pas de commentaires de style.
```

**Exemple — `.github/copilot/instructions/python.instructions.md` :**

```markdown
---
applyTo: "**/*.py"
---

- Utilise toujours les type hints (Python 3.10+).
- Les fonctions de plus de 20 lignes méritent une décomposition.
- Préfère `pathlib.Path` à `os.path`.
- Les exceptions doivent être spécifiques (pas de `except Exception` nu).
```

**Comment un coéquipier l'utilise :**

1. Il clone le repo.
2. Dans le chat Copilot de VS Code, il tape `/` pour voir les prompt files disponibles.
3. Il sélectionne `code-review` → le prompt est pré-rempli.

### 2.3 Custom agents / custom chat modes

> ℹ️ Les **custom agents** et **chat modes** sont des fonctionnalités avancées de VS Code
> Copilot (disponibles selon la version). Vérifie la documentation VS Code pour la syntaxe
> exacte de ta version.

**Emplacement :** `.github/copilot/agents/` ou `.vscode/`

**Exemple — `.github/copilot/agents/pr-reviewer.md` :**

```markdown
---
name: PR Reviewer
description: Agent de revue de pull request
tools:
  - githubRepo
  - codeSearch
---

Tu es un expert en revue de code Python.
Quand on te demande de relire une PR :
1. Lis le diff.
2. Liste les risques par ordre de priorité.
3. Propose les tests manquants.
4. Rédige un commentaire de review en markdown.

Ne commente pas le style si les tests passent.
```

---

## 3. Partage via Claude / Claude Code

### 3.1 Structure du dossier `.claude/`

Claude Code lit automatiquement les fichiers dans `.claude/` à la racine du projet.
Ce dossier est versionné avec le repo — c'est le mécanisme principal de partage.

**Structure recommandée :**

```text
.claude/
├── CLAUDE.md          ← instructions globales pour Claude sur ce projet
├── agents/
│   ├── reviewer.md    ← sous-agent spécialisé en revue
│   └── tester.md      ← sous-agent spécialisé en tests
└── skills/
    ├── lint-fixer.md  ← skill isolée : corriger les erreurs de lint
    └── doc-writer.md  ← skill isolée : rédiger la documentation
```

### 3.2 `CLAUDE.md` — instructions globales du projet

**Emplacement :** `.claude/CLAUDE.md` (ou `CLAUDE.md` à la racine)

Ce fichier est l'équivalent de `.github/copilot-instructions.md` pour Claude. Il est
automatiquement injecté dans le contexte de Claude Code quand il travaille sur le projet.

**Exemple de `.claude/CLAUDE.md` :**

```markdown
# MonProjet — Instructions Claude

## Présentation du projet
API REST Python (FastAPI 0.110+), tests pytest, déploiement Docker.
Base de données PostgreSQL, migrations Alembic.

## Conventions de code
- Python 3.11+ avec type hints complets
- Tests dans `tests/`, un fichier de test par module
- Variables d'environnement dans `.env.example` (jamais de secrets en dur)
- Branches : `feat/`, `fix/`, `chore/` + description courte

## Comportement attendu
- Toujours proposer des tests avec le code
- Valider les changements avec `pytest` avant de conclure
- Signaler les risques de sécurité avant toute autre remarque
- Ne jamais écrire de secrets dans les fichiers (utiliser os.environ)

## Commandes utiles
- Tests : `pytest tests/ -v`
- Lint : `ruff check .`
- Serveur dev : `uvicorn app.main:app --reload`
```

### 3.3 Définir et partager des skills isolées

Une **skill** est un fichier markdown qui décrit une capacité spécialisée de l'agent.

**Exemple — `.claude/skills/test-generator.md` :**

```markdown
# Skill : Générateur de tests pytest

## Rôle
Générer des tests unitaires complets pour une fonction Python.

## Comportement
1. Analyser la signature de la fonction et ses docstrings.
2. Identifier les cas nominaux, les cas limites et les cas d'erreur.
3. Générer des tests pytest avec des noms descriptifs.
4. Utiliser des fixtures si plusieurs tests partagent le même setup.
5. Annoter les tests avec des commentaires expliquant le scénario testé.

## Contraintes
- Ne pas modifier le code de production.
- Couvrir au minimum : cas nominal, valeur limite basse, valeur limite haute, entrée nulle.
- Utiliser `pytest.raises` pour les exceptions attendues.
- Ne jamais inventer le comportement attendu : demander si incertain.

## Format de sortie
```python
# cas nominal
def test_nom_fonction_cas_nominal():
    ...

# cas limite
def test_nom_fonction_valeur_vide():
    ...
```
```

**Partager UNIQUEMENT cette skill dans un autre repo :**

```bash
# Dans l'autre repo
mkdir -p .claude/skills
cp chemin/vers/repo-source/.claude/skills/test-generator.md .claude/skills/
git add .claude/skills/test-generator.md
git commit -m "feat: ajouter la skill test-generator depuis repo-source"
```

### 3.4 Définir des sous-agents

Un **sous-agent** est un agent spécialisé qui peut être appelé par un agent superviseur
ou utilisé directement par Claude Code.

**Exemple — `.claude/agents/reviewer.md` :**

```markdown
# Sous-agent : Reviewer

## Rôle
Effectuer une revue de code ciblée sur les risques (bugs, sécurité, tests manquants).

## Périmètre
- Analyse uniquement le diff ou les fichiers explicitement fournis.
- Ne commente pas le style (PEP 8, nommage) sauf si demandé.
- Signale l'incertitude si le contexte métier manque.

## Sorties attendues
1. **Résumé** : 2-3 phrases sur l'objectif du changement.
2. **Risques** : liste priorisée (🔴 critique, 🟡 moyen, 🟢 mineur).
3. **Tests manquants** : cas non couverts identifiés.
4. **Verdict** : ✅ Approuvé / ⚠️ Approuvé avec réserves / ❌ Changements requis.

## Garde-fous
- Ne jamais inventer un fichier absent du contexte.
- Ne jamais suggérer une action destructive sans avertissement explicite.
```

### 3.5 Config niveau projet vs niveau utilisateur

| Niveau | Emplacement | Partagé ? | Contenu typique |
|--------|-------------|-----------|-----------------|
| **Projet** | `.claude/` dans le repo | ✅ Oui (via Git) | Instructions repo, skills, agents |
| **Utilisateur** | `~/.claude/` sur ta machine | ❌ Non | Préférences personnelles, clés API |
| **Global utilisateur** | Settings Claude Desktop | ❌ Non | Comportement par défaut |

> ⚠️ Ne committe jamais `~/.claude/` dans le repo. Seul `.claude/` (local au projet)
> doit être versionné.

---

## 4. Bonnes pratiques d'industrialisation

### 4.1 Versionner et documenter

```text
.github/
├── copilot-instructions.md     ← instructions Copilot partagées
└── copilot/
    ├── prompts/                ← prompt files versionnés
    └── instructions/           ← instructions files versionnés
.claude/
├── CLAUDE.md                   ← instructions Claude versionnées
├── agents/                     ← sous-agents versionnés
└── skills/                     ← skills versionnées
```

**Bonne pratique** : ajoute une section dans le `README.md` du repo qui liste les agents
et skills disponibles :

```markdown
## 🤖 Agents et Skills disponibles

### GitHub Copilot
- **code-review** : revue ciblée risques (`.github/copilot/prompts/code-review.prompt.md`)
- **test-generator** : génération pytest (`.github/copilot/prompts/test-generator.prompt.md`)

### Claude Code
- **reviewer** : sous-agent de revue (`.claude/agents/reviewer.md`)
- **test-generator** : skill tests pytest (`.claude/skills/test-generator.md`)
```

### 4.2 Conventions de nommage

| Fichier | Convention | Exemple |
|---------|------------|---------|
| Prompt file Copilot | `kebab-case.prompt.md` | `code-review.prompt.md` |
| Instructions file | `contexte.instructions.md` | `python.instructions.md` |
| Skill Claude | `verbe-objet.md` | `generate-tests.md` |
| Agent Claude | `role.md` | `reviewer.md` |

### 4.3 Gérer les secrets et la configuration

```text
❌ NE JAMAIS faire :
.claude/CLAUDE.md :
  "Utilise la clé ANTHROPIC_API_KEY=sk-ant-xyz123 pour appeler l'API"

✅ Faire à la place :
.claude/CLAUDE.md :
  "La clé API est dans la variable d'environnement ANTHROPIC_API_KEY.
   Ne jamais la mettre en dur dans le code."

.env.example (commit ce fichier) :
  ANTHROPIC_API_KEY=your_key_here
  DB_HOST=localhost

.env (ne JAMAIS committer ce fichier, l'ajouter dans .gitignore) :
  ANTHROPIC_API_KEY=sk-ant-xyz123_real_key
```

### 4.4 Distribuer une skill isolée

**Option A — Copie directe** (simple, pour un usage ponctuel) :

```bash
cp .claude/skills/test-generator.md ../autre-projet/.claude/skills/
```

**Option B — Dossier autonome** (pour une skill complexe avec exemples) :

```text
skills/
└── test-generator/
    ├── README.md          ← documentation de la skill
    ├── skill.md           ← le fichier principal à copier dans .claude/skills/
    └── exemples/
        └── exemple_usage.md
```

**Option C — Package Git avec sous-modules** (pour une organisation qui partage des
skills entre plusieurs repos) :

```bash
# Dans le repo "skills-communs"
git init skills-communs
# ... ajouter les skills ...

# Dans un repo qui veut les utiliser
git submodule add https://github.com/org/skills-communs .claude/shared-skills
```

### 4.5 Gérer les mises à jour

- **Versionner les skills** dans le `CHANGELOG.md` ou les commit messages.
- **Tagger** les versions importantes : `git tag v1.2.0-skills`.
- **Documenter les changements** : ajoute une section `## Historique` en bas de chaque
  fichier skill si tu veux tracer les modifications importantes.

---

## 5. Guide pas à pas reproductible

### 5.1 Créer un agent + une skill → le committer → un coéquipier l'utilise

**Sur ta machine :**

```bash
# 1. Créer la structure dans le repo existant
mkdir -p .github/copilot/prompts
mkdir -p .claude/skills .claude/agents

# 2. Créer le fichier d'instructions Copilot global
cat > .github/copilot-instructions.md << 'EOF'
# Mon Projet — Instructions Copilot

## Contexte
Projet Python FastAPI. Tests avec pytest. Style PEP 8 + type hints.

## Comportement attendu
- Propose toujours des tests avec le code.
- Signale les risques de sécurité en premier.
- Ne modifie pas les fichiers hors scope.
EOF

# 3. Créer une skill isolée pour Claude
cat > .claude/skills/test-generator.md << 'EOF'
# Skill : Générateur de tests pytest

Génère des tests pytest complets pour une fonction Python.
Couvre : cas nominal, cas limites, cas d'erreur.
Ne modifie pas le code de production.
EOF

# 4. Créer un prompt file pour Copilot
cat > .github/copilot/prompts/generate-tests.prompt.md << 'EOF'
---
mode: ask
description: Générer des tests pytest pour la sélection
---

Génère des tests pytest pour le code sélectionné.
Couvre : cas nominal, valeurs limites, cas d'erreur.
Utilise des noms de tests descriptifs.
EOF

# 5. Committer et pousser
git add .github/ .claude/
git commit -m "feat: ajouter instructions Copilot, skill test-generator et prompt generate-tests"
git push
```

**Sur la machine du coéquipier :**

```bash
# 1. Cloner (ou puller le repo existant)
git clone https://github.com/org/mon-projet.git
cd mon-projet

# 2. Ouvrir VS Code
code .

# → Copilot utilise automatiquement .github/copilot-instructions.md
# → Dans le chat Copilot : taper "/" pour voir le prompt "generate-tests"

# 3. Utiliser Claude Code
claude
# → Claude lit automatiquement .claude/ et les skills sont disponibles
# → Demander : "Utilise la skill test-generator pour générer des tests pour auth.py"
```

### 5.2 Arborescence finale d'un projet bien outillé

```text
mon-projet/
├── .github/
│   ├── copilot-instructions.md          ← instructions globales Copilot
│   └── copilot/
│       ├── prompts/
│       │   ├── code-review.prompt.md    ← /code-review dans Copilot chat
│       │   └── generate-tests.prompt.md ← /generate-tests dans Copilot chat
│       └── instructions/
│           └── python.instructions.md   ← appliqué aux fichiers .py
├── .claude/
│   ├── CLAUDE.md                        ← instructions globales Claude
│   ├── agents/
│   │   └── reviewer.md                  ← sous-agent de revue
│   └── skills/
│       ├── test-generator.md            ← skill : générer des tests
│       └── doc-writer.md                ← skill : rédiger la documentation
├── .env.example                         ← modèle de config (sans secrets)
├── .gitignore                           ← inclut .env et les secrets locaux
├── README.md                            ← documenter les agents disponibles
└── src/
    └── ...
```

---

## ✅ Auto-évaluation

1. Quelle est la différence entre une config **personnelle** et une config **partagée** ?
<details><summary>Réponse</summary>La config personnelle vit sur ta machine (~/.claude/, paramètres VS Code utilisateur) et ne profite qu'à toi. La config partagée vit dans le repo Git (.github/, .claude/) et est disponible pour toute l'équipe dès qu'elle clone le repo.</details>

2. Comment partager **une seule skill** Claude dans un autre projet ?
<details><summary>Réponse</summary>Copie le fichier .md de la skill (.claude/skills/ma-skill.md) dans le dossier .claude/skills/ de l'autre projet et committe-le. La skill sera disponible dès que le repo est cloné ou mis à jour.</details>

3. À quoi sert `.github/copilot-instructions.md` ?
<details><summary>Réponse</summary>C'est un fichier lu automatiquement par GitHub Copilot pour tous les membres de l'équipe. Il définit le contexte du projet, les conventions et le comportement attendu de Copilot.</details>

4. Où ne faut-il **jamais** mettre les clés API et secrets ?
<details><summary>Réponse</summary>Jamais dans les fichiers versionnés (CLAUDE.md, copilot-instructions.md, code source). Ils doivent être dans des variables d'environnement ou un fichier .env qui est dans le .gitignore.</details>

5. Quelle est la différence entre un **prompt file** et une **instructions file** dans Copilot ?
<details><summary>Réponse</summary>Un prompt file (.prompt.md) définit un prompt réutilisable invocable via "/" dans le chat Copilot. Une instructions file (.instructions.md) définit des instructions qui s'appliquent automatiquement dans un contexte de fichier (ex. tous les fichiers .py).</details>

---

## ➡️ Pour aller plus loin

- [TP5 — Industrialiser & partager un agent](../module-4-tps/tp5/README.md)
- [Module 6 — Sécurité & gouvernance](../module-6-avance/README.md) : gestion des permissions
- Documentation officielle :
  - [GitHub Copilot customization](https://docs.github.com/copilot/customizing-copilot)
  - [Claude Code — CLAUDE.md](https://docs.anthropic.com/claude-code)
