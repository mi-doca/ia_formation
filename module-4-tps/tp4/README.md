# TP4 — Construire un serveur MCP custom et le consommer

## 🎯 Objectifs d'apprentissage

- Déclarer un serveur MCP minimal en Python.
- Exposer un tool clair et sûr.
- Générer un exemple de configuration client.

## ⏱️ Durée estimée

1 h 15 à 1 h 45.

## ✅ Prérequis

- Module 2 compris.
- Package `mcp` installé.

---

## Énoncé

Crée un serveur MCP qui expose un tool `read_release_notes(version)`.
Puis ajoute un script qui génère un exemple de configuration client pour Claude Desktop.

### Contraintes

- pas de secret en dur ;
- tool très simple et lisible ;
- sortie explicite ;
- un seul rôle par tool.

---

## Code fourni

- [`starter/server.py`](./starter/server.py)
- [`starter/client_example.py`](./starter/client_example.py)
- corrigés équivalents dans `corrige/`

### Exécution du corrigé

```bash
python module-4-tps/tp4/corrige/client_example.py
```

> Pour lancer réellement le serveur, installe `mcp` puis exécute `python module-4-tps/tp4/corrige/server.py`.

---

## ✅ Auto-évaluation

1. Pourquoi limiter un tool à une seule responsabilité ?
<details><summary>Réponse</summary>Pour faciliter la compréhension, la sécurité, les tests et la réutilisation.</details>

2. Pourquoi un exemple de configuration client est-il utile ?
<details><summary>Réponse</summary>Parce qu'un serveur MCP n'apporte de valeur que s'il peut être branché simplement dans un client réel.</details>

3. Pourquoi éviter les secrets en dur dans un serveur MCP ?
<details><summary>Réponse</summary>Parce qu'il est potentiellement partagé, versionné et exécuté dans plusieurs environnements.</details>

---

## ➡️ TP suivant

Passe au [TP5 — Industrialiser & partager un agent](../tp5/README.md).
