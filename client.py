import asyncio

from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client


async def main():

    server_params = StdioServerParameters(
        command="python",
        args=["server.py"],
    )

    async with stdio_client(server_params) as (read, write):

        async with ClientSession(read, write) as session:

            await session.initialize()

            tools = await session.list_tools()

            print("Available tools:")
            for tool in tools.tools:
                print(f"  - {tool.name}")

            print("\nTesting calculator...\n")

            result = await session.call_tool(
                "add",
                {"a": 10, "b": 20}
            )
            print("10 + 20 =", result)

            result = await session.call_tool(
                "subtract",
                {"a": 20, "b": 5}
            )
            print("20 - 5 =", result)

            result = await session.call_tool(
                "multiply",
                {"a": 10, "b": 5}
            )
            print("10 × 5 =", result)

            result = await session.call_tool(
                "divide",
                {"a": 20, "b": 4}
            )
            print("20 ÷ 4 =", result)


if __name__ == "__main__":
    asyncio.run(main())