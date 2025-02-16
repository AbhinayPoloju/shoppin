# examples/task_c.py

import asyncio
from agent.agent import ShoppingAgent

async def run_task_c():
    agent = ShoppingAgent()
    query = "I found a 'casual denim jacket' at $80 on SiteA. Any better deals?"
    response = await agent.respond(query)
    print("Task C Response:")
    print(response)

if __name__ == "__main__":
    asyncio.run(run_task_c())