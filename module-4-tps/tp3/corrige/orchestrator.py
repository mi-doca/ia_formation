from __future__ import annotations

import json



def worker_analysis(issue_text: str) -> dict:
    """Produit une lecture fonctionnelle rapide de l'incident."""
    return {
        "angle": "analyse",
        "resume": issue_text,
        "hypothese": "un changement récent a cassé une dépendance ou un chemin d'import",
    }



def worker_tests(issue_text: str) -> dict:
    """Propose les validations minimales à lancer."""
    return {
        "angle": "tests",
        "actions": [
            "relancer le job fautif en local",
            "exécuter les tests unitaires du package concerné",
            "ajouter un test de non-régression sur l'import manquant",
        ],
    }



def worker_risks(issue_text: str) -> dict:
    """Liste les risques de livraison associés à l'incident."""
    return {
        "angle": "risques",
        "points": [
            "blocage des merges",
            "augmentation du temps de correction en urgence",
            "risque de correctif incomplet si la cause racine est mal identifiée",
        ],
    }



def supervisor(issue_text: str) -> dict:
    """Orchestre les workers et fusionne leur sortie."""
    analysis = worker_analysis(issue_text)
    tests = worker_tests(issue_text)
    risks = worker_risks(issue_text)
    return {
        "demande": issue_text,
        "synthese": "Incident CI à traiter en priorité avant de poursuivre les livraisons.",
        "contributions": [analysis, tests, risks],
    }


if __name__ == "__main__":
    sample = "Le pipeline CI échoue après fusion sur la branche main à cause d'un import manquant."
    print(json.dumps(supervisor(sample), ensure_ascii=False, indent=2))
