# examples/task_e.py

import asyncio
import os
import sys
from pathlib import Path
sys.path.append(str(Path(__file__).parent.parent))
from agent.agent import ShoppingAgent

async def run_task_e():
    agent = ShoppingAgent()
    query = "Find a floral skirt under $40 in size S that can arrive by Friday.Check if there are any better deals.Is it in stock, and can I apply a discount code 'SAVE10'?Returns should be hassle-free. Do they accept returns? "
    response = await agent.respond(query)
    print("Task E Response:")
    print(response)

if __name__ == "__main__":
    asyncio.run(run_task_e())