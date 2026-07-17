# Module 5 — IA dans le cycle de vie logiciel

## 🎯 Objectifs d'apprentissage

- Identifier où l'IA agentique aide réellement dans un SDLC.
- Concevoir des usages concrets pour tickets, dev, tests, CI/CD et outillage interne.
- Comprendre les garde-fous nécessaires avant la mise en production.

## ⏱️ Durée estimée

2 h 30 à 3 h.

## ✅ Prérequis

- Avoir parcouru les modules 0 à 4.
- Être familier avec Git, pull requests et tests Python.

---

## 1. Créer des tickets / issues de meilleure qualité

Un agent peut transformer :

- un échange Slack ;
- un log d'incident ;
- une demande utilisateur ;
- une note de réunion ;

… en **issue structurée**.

### Gabarit utile

- **Titre** : orienté problème.
- **Contexte** : où, quand, sur quoi.
- **Impact** : utilisateur, métier, technique.
- **Reproduction** : étapes minimales.
- **Critères d'acceptation** : vérifiables.

### Prompt type

```text
Tu es un assistant de triage logiciel.
Transforme les notes suivantes en issue GitHub.
Contraintes : titre court, reproduction, impact, critères d'acceptation, pas d'invention.
```

---

## 2. Développement assisté

L'IA agentique peut aider à :

- proposer un plan de modification ;
- implémenter un changement localisé ;
- expliquer un diff ;
- faire une revue ciblée ;
- préparer une PR plus lisible.

### Bonne pratique avec un coding agent

1. cadrer une tâche précise ;
2. fournir fichiers, contraintes et critères de validation ;
3. demander un plan ;
4. exiger une validation par tests ;
5. relire le diff avant fusion.

> L'agent accélère. Il ne remplace pas le jugement d'ingénierie.

---

## 3. Tests unitaires avec pytest

Les agents sont très utiles pour :

- lister cas nominaux et cas limites ;
- transformer des exemples métier en tests ;
- maintenir des tests après refactoring ;
- repérer les assertions manquantes.

### Exemple Python

```python
def normalize_branch_name(name: str) -> str:
    return name.strip().lower().replace(" ", "-")
```

Prompt utile :

```text
Propose des tests pytest pour cette fonction.
Couvre cas nominal, espaces multiples, chaîne vide et caractères déjà normalisés.
```

### Limite fréquente

L'IA propose parfois des tests qui reflètent **son hypothèse** du comportement,
pas forcément le comportement voulu. Il faut donc relire les attentes métier.

---

## 4. CI/CD : intégrer des agents dans GitHub Actions

Usages possibles :

- résumé automatique d'une PR ;
- génération d'issue si le build échoue ;
- classification d'un changelog ;
- aide au triage sécurité.

### Exemple de workflow

```yaml
name: ai-pr-summary
on:
  pull_request:
    types: [opened, synchronize]

jobs:
  summarize:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - name: Générer un résumé de PR
        run: echo "Ici, un agent pourrait résumer le diff ou préparer un commentaire."
```

### Garde-fous CI

- secrets strictement limités ;
- permissions GitHub minimales ;
- validation humaine pour les actions sensibles ;
- logs observables et faciles à auditer.

---

## 5. MCP en production

En production, MCP permet à un agent d'accéder à des outils internes **sans tout recoder** dans le prompt.

### Cas d'usage

- lire l'état d'un service ;
- consulter un runbook ;
- créer un brouillon de ticket ;
- récupérer un historique d'incidents.

### Principe du moindre privilège

Expose seulement ce qui est nécessaire :

- lecture avant écriture ;
- prévisualisation avant mutation ;
- données filtrées plutôt que brutes.

---

## 6. Exemple de workflow bout en bout

```text
Signal faible -> agent de triage -> issue structurée -> agent de dev -> tests -> CI -> revue humaine -> livraison
```

La valeur ne vient pas d'un super-agent unique, mais de l'**enchaînement maîtrisé** des étapes.

---

## ✅ Auto-évaluation

1. Que doit contenir une bonne issue générée par IA ?
<details><summary>Réponse</summary>Un titre clair, le contexte, l'impact, la reproduction et des critères d'acceptation vérifiables.</details>

2. Pourquoi faut-il relire les tests générés par IA ?
<details><summary>Réponse</summary>Parce qu'ils peuvent refléter une hypothèse erronée du comportement attendu.</details>

3. Quel garde-fou est essentiel en CI/CD ?
<details><summary>Réponse</summary>Le principe du moindre privilège, complété par une validation humaine sur les actions sensibles.</details>

4. Quel est l'intérêt de MCP en production ?
<details><summary>Réponse</summary>Connecter proprement les agents aux outils internes via une interface standardisée et gouvernable.</details>

5. Où l'agent apporte le plus de valeur dans le SDLC ?
<details><summary>Réponse</summary>Sur les tâches répétitives, structurantes ou riches en contexte : triage, synthèse, génération de tests, lecture de logs, préparation d'artefacts.</details>

---

## ➡️ Module suivant

Passe au [Module 6 — Sujets avancés & bonnes pratiques](../module-6-avance/README.md).
