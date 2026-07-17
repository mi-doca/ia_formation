from mcp.server.fastmcp import FastMCP

mcp = FastMCP("release-notes-server")

RELEASE_NOTES = {
    "1.0.0": "Première version stable du service.",
    "1.1.0": "Ajout du mode batch pour les traitements agentiques.",
    "1.2.0": "Amélioration des logs et de la robustesse des retries.",
}


@mcp.tool()
def read_release_notes(version: str) -> str:
    """Retourne une note de version courte et lisible."""
    return RELEASE_NOTES.get(version, "Version inconnue.")


if __name__ == "__main__":
    mcp.run()
