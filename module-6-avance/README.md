# Module 6 — Sujets avancés & bonnes pratiques

## 🎯 Objectifs d'apprentissage

- Identifier les principaux risques de sécurité des agents.
- Mettre en place une démarche d'**évaluation**.
- Optimiser les **coûts** et la latence.
- Comprendre la **gouvernance** et l'observabilité nécessaires en contexte pro.

## ⏱️ Durée estimée

2 h 30 à 3 h.

## ✅ Prérequis

- Avoir parcouru tout le parcours jusqu'au module 5.
- Être à l'aise avec les notions d'API, logs et workflows de développement.

---

## 1. Sécurité : la face non optionnelle de l'agentique

### Risques majeurs

- **prompt injection** : une donnée externe tente de détourner le comportement de l'agent ;
- **exfiltration** : le modèle révèle des données sensibles ;
- **sur-permission** : un tool donne trop de pouvoir ;
- **action non vérifiée** : l'agent modifie trop vite un système réel.

### Mesures de base

- instructions système claires ;
- filtrage des entrées ;
- séparation lecture / écriture ;
- validation humaine avant les mutations ;
- secrets via variables d'environnement uniquement.

---

## 2. Évaluation (evals)

Un agent utile n'est pas seulement impressionnant : il est **mesurable**.

### Ce qu'on peut mesurer

- exactitude ;
- taux de format correct ;
- nombre d'appels tools ;
- coût moyen ;
- temps de réponse ;
- besoin de reprise humaine.

### Mini boucle d'eval

1. définir 10 à 20 cas représentatifs ;
2. fixer un attendu ;
3. exécuter l'agent ;
4. comparer ;
5. ajuster prompt, tools ou orchestration.

### Exemple simple

```python
def is_issue_complete(text: str) -> bool:
    required = ["contexte", "impact", "reproduction", "critères d'acceptation"]
    lowered = text.lower()
    return all(section in lowered for section in required)
```

---

## 3. Coûts & optimisation

### Leviers classiques

- choisir un modèle plus petit quand c'est suffisant ;
- réduire le contexte injecté ;
- résumer l'historique ;
- éviter les appels tools inutiles ;
- utiliser le **prompt caching** quand c'est disponible ;
- batcher certaines tâches.

### Heuristique utile

- **petit modèle** pour classer, extraire, reformater ;
- **modèle moyen** pour synthétiser et coder des tâches bornées ;
- **gros modèle** pour diagnostic complexe, architecture, arbitrage ambigu.

---

## 4. Gouvernance

Un agent en entreprise doit rester dans un cadre lisible.

### Questions à poser

- qui a le droit de lancer cet agent ?
- sur quelles données ?
- avec quels tools ?
- quelles actions nécessitent un humain ?
- où sont stockés les logs ?

### Human-in-the-loop

Conserve une validation humaine pour :

- écrire dans un système de prod ;
- publier une issue ou une PR sensible ;
- lancer une action coûteuse ou destructrice ;
- partager une analyse sécurité.

---

## 5. Observabilité

Sans traces, tu ne sauras pas pourquoi un agent a réussi… ou échoué.

### À tracer

- prompt système et consignes clés (sans secrets) ;
- tools appelés ;
- durée ;
- volume de tokens ;
- erreurs ;
- décision finale.

### Outils possibles

- logs structurés JSON ;
- dashboards maison ;
- solutions de tracing agentique (selon ton stack).

---

## 6. Check-list avant mise en prod

- [ ] Objectif métier clair
- [ ] Permissions minimales
- [ ] Secrets hors code
- [ ] Jeux d'eval disponibles
- [ ] Coûts observés
- [ ] Logs activés
- [ ] Validation humaine sur les actions sensibles

---

## ✅ Auto-évaluation

1. Qu'est-ce qu'une prompt injection ?
<details><summary>Réponse</summary>Une tentative de détourner les instructions d'un agent via une entrée externe, comme un document ou un message utilisateur.</details>

2. Pourquoi les evals sont-elles importantes ?
<details><summary>Réponse</summary>Parce qu'elles permettent de mesurer la qualité réelle de l'agent au lieu de se fier à une impression ponctuelle.</details>

3. Cite deux leviers de réduction de coût.
<details><summary>Réponse</summary>Réduire le contexte injecté et choisir un modèle plus petit quand la tâche le permet.</details>

4. Pourquoi garder un humain dans la boucle ?
<details><summary>Réponse</summary>Pour contrôler les actions sensibles, limiter les erreurs et assumer la responsabilité métier.</details>

5. Que faut-il tracer pour observer un agent ?
<details><summary>Réponse</summary>Ses prompts, tools, durées, coûts, erreurs et décisions finales.</details>

---

## ➡️ Et après ?

- Refaire les [TPs du module 4](../module-4-tps/README.md) avec tes propres cas métier.
- Créer un premier serveur MCP relié à un outil interne en lecture seule.
- Construire une mini suite d'evals sur un usage réel de ton équipe.

---

## ⬅️ Module précédent

Revenir au [Module 5 — IA dans le cycle de vie logiciel](../module-5-sdlc/README.md).
