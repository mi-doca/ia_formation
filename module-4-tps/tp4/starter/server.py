from mcp.server.fastmcp import FastMCP

mcp = FastMCP("release-notes-server")


@mcp.tool()
def read_release_notes(version: str) -> str:
    raise NotImplementedError("À compléter pendant le TP")


if __name__ == "__main__":
    mcp.run()
