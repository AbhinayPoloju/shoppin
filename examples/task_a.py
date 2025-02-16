# examples/task_a.py

import asyncio
import os
import sys
from pathlib import Path
sys.path.append(str(Path(__file__).parent.parent))
from agent.agent import ShoppingAgent

async def run_task_a():
    agent = ShoppingAgent()
    query = "Find a floral skirt under $40 in size S. Is it in stock, and can I apply a discount code 'SAVE10'?"
    response = await agent.respond(query)
    print("Task A Response:")
    print(response)

if __name__ == "__main__":
    asyncio.run(run_task_a())