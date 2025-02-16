# examples/task_d.py

import asyncio
import os
import sys
from pathlib import Path
sys.path.append(str(Path(__file__).parent.parent))
from agent.agent import ShoppingAgent

async def run_task_d():
    agent = ShoppingAgent()
    query = "I want to buy a cocktail dress from SiteB, but only if returns are hassle-free. Do they accept returns?"
    response = await agent.respond(query)
    print("Task D Response:")
    print(response)

if __name__ == "__main__":
    asyncio.run(run_task_d())