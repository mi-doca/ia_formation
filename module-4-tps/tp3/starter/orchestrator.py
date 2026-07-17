from __future__ import annotations


def worker_analysis(issue_text: str) -> dict:
    raise NotImplementedError("À compléter pendant le TP")


def worker_tests(issue_text: str) -> dict:
    raise NotImplementedError("À compléter pendant le TP")


def worker_risks(issue_text: str) -> dict:
    raise NotImplementedError("À compléter pendant le TP")


def supervisor(issue_text: str) -> dict:
    raise NotImplementedError("À compléter pendant le TP")


if __name__ == "__main__":
    sample = "Le pipeline CI échoue après fusion sur la branche main à cause d'un import manquant."
    print(supervisor(sample))
