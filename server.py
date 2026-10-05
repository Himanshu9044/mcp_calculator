from mcp.server.fastmcp import FastMCP
mcp=FastMCP("Calculator", "1.0.0", "A simple calculator plugin for FastMCP")
@mcp.tool()
def add(a: float, b: float) -> float:
    """Adds two numbers together."""
    return a + b

@mcp.tool()
def subtract(a: float, b: float) -> float:
    """Subtracts the second number from the first."""
    return a - b

@mcp.tool()
def multiply(a: float, b: float) -> float:
    """Multiplies two numbers together."""
    return a * b

@mcp.tool()
def divide(a: float, b: float) -> float:
    """Divides the first number by the second."""
    if b == 0:
        raise ValueError("Cannot divide by zero.")
    return a / b

@mcp.resource("Calculator", "1.0.0")
def get_calculator_info():
    """Returns information about the calculator plugin."""
    return {
        "name": "Calculator",
        "version": "1.0.0",
        "description": "A simple calculator plugin for FastMCP"
    }
    
if __name__ == "__main__":
    mcp.run()