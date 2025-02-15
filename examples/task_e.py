# examples/task_e.py

import asyncio
import sys
sys.path.append('/export/home/vivian/svarah/shoppin')
from agent.agent import ShoppingAgent

async def run_task_e():
    agent = ShoppingAgent()
    query = "Find a floral skirt under $40 in size S. Check if it can arrive by Friday, and apply the discount code 'SAVE10'."
    response = await agent.respond(query)
    print("Task E Response:")
    print(response)

if __name__ == "__main__":
    asyncio.run(run_task_e())