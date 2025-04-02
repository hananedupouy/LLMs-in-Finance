import asyncio
import shutil

from agents import Agent, Runner, trace
from agents.mcp import MCPServer, MCPServerStdio

async def run(mcp_server: MCPServer, repo_path: str):
    agent = Agent(
        name="Assistant",
        instructions=f"Respond to questions about the Git repository located at {repo_path}. Use this as the value for repo_path.",
        mcp_servers=[mcp_server],
        model = 'o3-mini'
    )

    messages = ["Summarize the different topics explored in this repo",
                "What are the different agents explored in this repo?",
                "What are the different frameworks used for agents in this repo?"]

    for message in messages:
        print("\n" + "-" * 40)
        print(f"Running: {message}")
        result = await Runner.run(starting_agent=agent, input=message)
        print(result.final_output)


async def main():
    repo_path = "https://github.com/hananedupouy/LLMs-in-Finance/"

    async with MCPServerStdio(
        cache_tools_list=True,  # Cache the tools list, for demonstration
        params={"command": "uvx", "args": ["mcp-server-git"]},
    ) as server:
        await run(server, repo_path)


if __name__ == "__main__":
    if not shutil.which("uvx"):
        raise RuntimeError("uvx is not installed. Please install it with `pip install uvx`.")

    asyncio.run(main())