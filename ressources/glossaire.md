# 📖 Glossaire de l'IA agentique

| Terme | Définition courte |
|-------|-------------------|
| **Agent** | Système piloté par un LLM capable de planifier, appeler des tools et boucler jusqu'à un objectif. |
| **Attention / self-attention** | Mécanisme par lequel chaque token peut pondérer les autres tokens du contexte pour construire une représentation plus utile. |
| **Chain-of-Thought** | Raisonnement étape par étape, parfois explicite, parfois gardé en interne selon l'outil. |
| **CI/CD** | Continuous Integration / Continuous Deployment : pipeline automatisé qui construit, teste et déploie le code à chaque changement. |
| **Context window / fenêtre de contexte** | Volume maximal de tokens visibles en une fois par le modèle. |
| **Contexte (liste de messages)** | L'ensemble des messages (system, user, assistant, tool) renvoyés au modèle à chaque tour. C'est ce contexte qui donne l'illusion de mémoire. |
| **Embedding** | Vecteur de départ associé à un token ou à un texte, utilisé pour le représenter sous forme numérique. |
| **Eval** | Évaluation mesurée d'un agent ou d'un prompt sur un ensemble de cas. |
| **Few-shot prompting** | Prompt contenant un petit nombre d'exemples. |
| **Fine-tuning** | Phase d'ajustement d'un modèle déjà pré-entraîné pour mieux suivre des instructions ou mieux se comporter dans un domaine donné. |
| **Function calling / tool calling** | Mécanisme par lequel le modèle propose l'appel structuré d'un outil externe. |
| **Hallucination** | Réponse plausible mais fausse ou non fondée. |
| **Human-in-the-loop** | Validation humaine à une étape clé d'un workflow automatisé. |
| **Inférence** | Moment où l'on utilise le modèle entraîné pour produire une réponse à partir d'un prompt. |
| **Instructions file** | Fichier `.instructions.md` dans un repo Copilot définissant des instructions qui s'appliquent automatiquement à un contexte de fichiers. |
| **LLM** | Modèle de langage de grande taille, spécialisé dans la prédiction du prochain token. |
| **MCP** | Model Context Protocol, protocole standard pour connecter clients et serveurs d'outils/resources/prompts. |
| **Mémoire court terme** | Informations présentes dans le contexte actif de la session. |
| **Mémoire long terme** | Informations stockées dans un système externe : base, wiki, vector store, fichiers, etc. |
| **OpenCode** | Agent CLI open source permettant de piloter un LLM depuis le terminal pour explorer, modifier et tester un dépôt, agnostique au fournisseur de modèle. |
| **Plan** | Décomposition explicite d'une tâche en étapes ordonnées. |
| **Prompt** | Texte ou message envoyé au modèle pour cadrer la génération. |
| **Prompt caching** | Réutilisation partielle d'un prompt déjà traité pour réduire coûts et latence quand le fournisseur le permet. |
| **Prompt file** | Fichier `.prompt.md` dans un repo Copilot définissant un prompt réutilisable invocable via "/" dans le chat. |
| **Prompt injection** | Tentative de détourner le comportement d'un agent via une instruction cachée dans ses entrées. |
| **Pré-entraînement** | Phase initiale où un modèle apprend sur une très grande quantité de texte, en général en prédisant le prochain token. |
| **RAG** | Retrieval Augmented Generation : récupération de contexte externe avant génération. |
| **ReAct** | Pattern agentique alternant raisonnement et action. |
| **Resource** | Donnée ou document exposé par un serveur MCP. |
| **Réseau de neurones** | Suite de couches de calcul qui transforment progressivement les vecteurs d'entrée en représentations plus utiles pour une tâche. |
| **Sampling / décodage** | Façon de choisir le prochain token à partir de la distribution de probabilités produite par le modèle. |
| **SDLC** | Software Development Lifecycle : ensemble des étapes du cycle de vie d'un logiciel (spécification, développement, tests, déploiement, maintenance). |
| **Skill / custom agent** | Agent ou jeu d'instructions réutilisable pour une tâche spécialisée. |
| **Sous-agent** | Agent spécialisé appelé par un agent superviseur. |
| **Stateless** | Sans état. Un LLM est stateless : il ne conserve aucune information entre deux appels API. La "mémoire" vient de l'historique renvoyé dans le contexte. |
| **System prompt** | Consigne de plus haut niveau qui fixe rôle, ton et contraintes. |
| **Température** | Paramètre contrôlant le niveau de variabilité des réponses. |
| **Token** | Unité de texte traitée par le modèle ; ce n'est pas toujours un mot complet. Un mot peut correspondre à un ou plusieurs tokens. |
| **Tool result** | Résultat renvoyé par l'exécution d'un tool, ajouté au contexte pour que le modèle puisse observer ce qui s'est passé. |
| **Top-p** | Paramètre de sampling qui limite la masse de probabilité considérée pour choisir le prochain token. |
| **Tool** | Action exécutable par un agent : lire un fichier, lancer un test, appeler une API, etc. |
| **Tour agentique** | Une itération de la boucle agentique : appel LLM → tool_use → tool_result → prochain appel LLM. |
| **Transformer** | Architecture de réseau de neurones très utilisée dans les LLM, fondée sur l'attention pour transformer les représentations de tous les tokens du contexte. |
| **Troncature** | Suppression des messages les plus anciens quand la liste de messages dépasse la fenêtre de contexte. |
| **Vecteur** | Liste de nombres utilisée pour représenter un token, un texte ou un état interne du modèle. |
| **Vector store** | Base stockant des embeddings pour retrouver rapidement des passages proches d'une requête. |
| **Distribution de probabilité** | Répartition des probabilités attribuées par le modèle aux différents tokens possibles à l'étape suivante. |
| **Zero-shot prompting** | Prompt sans exemple. |
