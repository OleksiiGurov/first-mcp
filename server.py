"""A minimal FastMCP server with one tool and one prompt, for smoke-testing deploys."""

from fastmcp import FastMCP

mcp = FastMCP("first-mcp")


@mcp.tool
def add(a: int, b: int) -> int:
    """Add two integers and return the result."""
    return a + b


@mcp.tool
def greet(name: str) -> str:
    """Return a friendly one-sentence greeting for the given name."""
    return f"Hello, {name}! Great to see you."


if __name__ == "__main__":
    mcp.run()
