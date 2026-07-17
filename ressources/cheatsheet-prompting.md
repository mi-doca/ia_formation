# 🧠 Cheatsheet prompting pour l'ingénierie logicielle

## 1. Structure de prompt simple et robuste

```text
Contexte : ...
Objectif : ...
Contraintes : ...
Sortie attendue : ...
Critères de qualité : ...
```

---

## 2. Template pour demander un plan

```text
Tu es un assistant d'ingénierie logicielle.
Contexte : dépôt Python, bug reproductible localement.
Objectif : proposer un plan de correction.
Contraintes : pas de modification hors périmètre, citer les fichiers probables, proposer des validations.
Sortie attendue :
1. compréhension du problème ;
2. hypothèses ;
3. plan en étapes ;
4. risques.
```

---

## 3. Template pour générer des tests

```text
Tu es spécialiste pytest.
Voici la fonction :
<code>
...
</code>
Génère des tests unitaires.
Contraintes : cas nominal, cas limites, erreurs, pas de dépendance réseau, pas de modification du code source.
```

---

## 4. Template pour revue de code

```text
Relis ce diff comme un reviewer senior.
Signale uniquement :
- bugs probables ;
- oublis de tests ;
- risques sécurité ;
- comportements non couverts.
Réponse concise, structurée, avec références de fichiers si disponibles.
```

---

## 5. Template pour créer une issue

```text
Transforme les notes suivantes en issue GitHub.
Attendus :
- titre ;
- contexte ;
- impact ;
- reproduction ;
- critères d'acceptation.
N'invente rien : si une information manque, écris "à préciser".
```

---

## 6. Template pour un agent avec tools

```text
Rôle : agent de diagnostic CI.
Objectif : expliquer pourquoi le pipeline échoue.
Tools autorisés : lecture des logs, lecture de fichiers, liste des jobs.
Interdits : écriture, suppression, actions réseau non prévues.
Quand tu manques d'information, demande un tool plutôt que spéculer.
```

---

## 7. Rappels pratiques

- Demande un **format de sortie** explicite.
- Donne les **contraintes** tôt.
- Préfère des tâches **petites et vérifiables**.
- En agentique, précise toujours les **tools autorisés** et les **garde-fous**.
- Pour les tâches sensibles, impose une étape **"demander validation avant action"**.
