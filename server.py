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

@mcp.resource("calculator://info")
def get_calculator_info() -> str:
    """Returns information about the calculator."""
    return """
    Calculator MCP Server
    Version: 1.0.0
    Operations: add, subtract, multiply, divide
    """
    


if __name__ == "__main__":
    print("Starting Calculator MCP Server...")
    mcp.run()