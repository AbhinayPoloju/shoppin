# examples/task_d.py

import asyncio
import sys
sys.path.append('/export/home/vivian/svarah/shoppin')
from agent.agent import ShoppingAgent

async def run_task_d():
    agent = ShoppingAgent()
    query = "I want to buy a cocktail dress from SiteB, but only if returns are hassle-free. Do they accept returns?"
    response = await agent.respond(query)
    print("Task D Response:")
    print(response)

if __name__ == "__main__":
    asyncio.run(run_task_d())