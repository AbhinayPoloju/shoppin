# examples/task_b.py

import asyncio
import sys
sys.path.append('/export/home/vivian/svarah/shoppin')
from agent.agent import ShoppingAgent

async def run_task_b():
    agent = ShoppingAgent()
    query = "I need white sneakers (size 8) for under $70 that can arrive by Friday."
    response = await agent.respond(query)
    print("Task B Response:")
    print(response)

if __name__ == "__main__":
    asyncio.run(run_task_b())