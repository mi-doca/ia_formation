# Module 4 — TPs pratiques

## 🎯 Objectifs d'apprentissage

- Passer de la théorie à la pratique.
- Construire un premier agent, puis des patterns plus avancés.
- Produire des artefacts réutilisables : instructions, orchestrateurs, serveur MCP, package.

## ⏱️ Durée estimée

6 h à 10 h selon le niveau d'approfondissement.

## ✅ Prérequis

- Avoir parcouru les modules 0 à 3.
- Avoir Python 3.10+ et installé les dépendances de [`requirements.txt`](../requirements.txt).

---

## Organisation des TPs

Chaque TP contient :

- un `README.md` avec l'énoncé ;
- un dossier `starter/` pour démarrer ;
- un dossier `corrige/` pour comparer ou débloquer.

| TP | Sujet | Livrable principal |
|----|-------|--------------------|
| [TP1](./tp1/README.md) | Premier agent avec function calling | `agent.py` |
| [TP2](./tp2/README.md) | Skills / custom agents | fichiers d'instructions + linter |
| [TP3](./tp3/README.md) | Sous-agents et orchestration | `orchestrator.py` |
| [TP4](./tp4/README.md) | Serveur MCP custom | `server.py` + exemple client |
| [TP5](./tp5/README.md) | Industrialiser et partager un agent | package Python minimal |

---

## Conseils de réalisation

1. Fais d'abord le **starter** sans regarder le corrigé.
2. Exécute ton code à chaque petite étape.
3. Compare ensuite avec le corrigé : structure, lisibilité, sécurité, configurabilité.
4. Note ce que tu réutiliserais dans un vrai projet.

---

## Commandes utiles

```bash
python module-4-tps/tp1/corrige/agent.py
python module-4-tps/tp2/corrige/prompt_linter.py module-4-tps/tp2/corrige
python module-4-tps/tp3/corrige/orchestrator.py
python module-4-tps/tp5/corrige/src/agent_factory/cli.py scaffold --name reviewer
```

> Le TP4 nécessite le package `mcp` pour une exécution complète.

---

## ✅ Auto-évaluation

1. Pourquoi les TPs sont-ils structurés en starter + corrigé ?
<details><summary>Réponse</summary>Pour pratiquer activement avant de comparer avec une implémentation de référence.</details>

2. Quel TP te fait travailler MCP ?
<details><summary>Réponse</summary>Le TP4.</details>

3. Quel TP te fait réfléchir à l'industrialisation ?
<details><summary>Réponse</summary>Le TP5.</details>

4. Pourquoi exécuter les exemples à chaque étape ?
<details><summary>Réponse</summary>Pour détecter tôt les erreurs de conception, de syntaxe ou de compréhension.</details>

---

## ➡️ Module suivant

Après les TPs, poursuis avec [Module 5 — IA dans le cycle de vie logiciel](../module-5-sdlc/README.md).
