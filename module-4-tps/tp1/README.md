# TP1 — Premier agent Python avec function calling

## 🎯 Objectifs d'apprentissage

- Définir deux tools simples.
- Simuler une boucle agentique minimale.
- Produire une réponse finale à partir des résultats de tools.

## ⏱️ Durée estimée

45 min à 1 h 15.

## ✅ Prérequis

- Module 1 compris.
- Bases Python : fonctions, dictionnaires, `if __name__ == "__main__"`.

---

## Énoncé

Construis un mini agent capable de :

1. détecter une demande de calcul (`+` ou `*`) ;
2. détecter une demande météo mockée pour `Paris`, `Lyon` ou `Marseille` ;
3. exécuter les tools nécessaires ;
4. renvoyer une synthèse finale en français.

### Contraintes

- pas de clé API requise ;
- pas de secret en dur ;
- comportement déterministe ;
- code clair et commenté.

---

## Étapes suggérées

1. Complète les tools.
2. Implémente une étape de "planification" très simple basée sur des règles.
3. Exécute chaque tool demandé.
4. Génère une réponse finale lisible.

---

## Code fourni

- [`starter/agent.py`](./starter/agent.py)
- [`corrige/agent.py`](./corrige/agent.py)

### Exécution du corrigé

```bash
python module-4-tps/tp1/corrige/agent.py
```

---

## ✅ Auto-évaluation

1. Qu'est-ce qui différencie ici un agent d'un simple script ?
<details><summary>Réponse</summary>La séparation compréhension -> choix des actions -> exécution des tools -> synthèse finale.</details>

2. Pourquoi utiliser une météo mockée ?
<details><summary>Réponse</summary>Pour apprendre la boucle agentique sans dépendre d'une API externe ni d'une clé secrète.</details>

3. Que gagnerais-tu à remplacer la planification par un vrai LLM ?
<details><summary>Réponse</summary>Plus de flexibilité dans la compréhension, mais aussi plus de coût, de variance et de garde-fous à prévoir.</details>

---

## ➡️ TP suivant

Passe au [TP2 — Skills / custom agents](../tp2/README.md).
