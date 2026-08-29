"""A minimal FastMCP server with one tool and one prompt, for smoke-testing deploys."""

from fastmcp import FastMCP

mcp = FastMCP("first-mcp")


@mcp.tool
def add(a: int, b: int) -> int:
    """Add two integers and return the result."""
    return a + b


@mcp.prompt
def greet(name: str) -> str:
    """Generate a friendly greeting prompt for the given name."""
    return f"Say a warm, one-sentence hello to {name}."


if __name__ == "__main__":
    mcp.run()
