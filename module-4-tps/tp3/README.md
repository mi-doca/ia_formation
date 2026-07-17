# TP3 — Orchestrer des sous-agents

## 🎯 Objectifs d'apprentissage

- Comprendre le rôle d'un superviseur.
- Décomposer une tâche en workers spécialisés.
- Fusionner plusieurs points de vue en une synthèse unique.

## ⏱️ Durée estimée

1 h à 1 h 30.

## ✅ Prérequis

- Module 1 compris.
- Notions de fonctions Python et de listes.

---

## Énoncé

Construis un orchestrateur qui reçoit une description d'incident ou de ticket,
puis délègue à trois sous-agents simulés :

- analyse du problème ;
- stratégie de tests ;
- risques de livraison.

Le superviseur doit ensuite renvoyer un objet unique lisible.

---

## Code fourni

- [`starter/orchestrator.py`](./starter/orchestrator.py)
- [`corrige/orchestrator.py`](./corrige/orchestrator.py)

### Exécution du corrigé

```bash
python module-4-tps/tp3/corrige/orchestrator.py
```

---

## ✅ Auto-évaluation

1. Pourquoi séparer les rôles en workers ?
<details><summary>Réponse</summary>Pour spécialiser le raisonnement et réduire la complexité de chaque sous-tâche.</details>

2. Quel est le rôle du superviseur ?
<details><summary>Réponse</summary>Il distribue la demande, récupère les contributions et produit la synthèse finale.</details>

3. Quel est le risque d'un multi-agent mal conçu ?
<details><summary>Réponse</summary>Ajouter du coût, du bruit et de la coordination inutile sans gain réel.</details>

---

## ➡️ TP suivant

Passe au [TP4 — Construire un serveur MCP](../tp4/README.md).
