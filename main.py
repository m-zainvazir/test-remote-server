from fastmcp import FastMCP
import random
import json

mcp  = FastMCP(name="Simple calculator Server")

#Tool 1: Add two numbers
@mcp.tool
def add_numbers(a: int, b: int) -> int:
    """Add 2 numbers together
    Args:
        a (int): First number   
        b (int): Second number
    Returns:
        int: The sum of the two numbers
    
    """
    return a + b

# Tool 2: Generate a random number
@mcp.tool
def generate_random_number(min_value: int=0, max_value: int=100) -> int:
    """Generate a random number between min_value and max_value
    Args:
        min_value (int, optional): Minimum value. Defaults to 0.
        max_value (int, optional): Maximum value. Defaults to 100.
    Returns:
        int: Random number between min_value and max_value
    """
    return random.randint(min_value, max_value)

# Resource: Server Info
@mcp.resource("info://server")
def server_info() -> dict:
    """Return server information."""
    info= {
        "name": "Simple Calculator Server",
        "version": "1.0",
        "description": "A simple MCP server with math tools.",
        "tools": ["add_numbers", "generate_random_number"],
        "author": "Your Name"
    }
    return json.dumps(info, indent=2)

#Start the MCP server
if __name__ == "__main__":
    mcp.run(transport="http", host="0.0.0.0", port=8000)

