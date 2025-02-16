# main.py

import asyncio
from agent.agent import ShoppingAgent

async def main():
    agent = ShoppingAgent()
    
    # Task A: Basic Item Search + Price Constraint
    query1 = "Find a floral skirt under $40 in size S. Is it in stock, and can I apply a discount code 'SAVE10'?"
    print("\n=== Task A: Basic Search + Discount ===")
    print("Query:", query1)
    response1 = await agent.respond(query1)
    print("Response:", response1)

    # Task B: Shipping Deadline
    query2 = "I need white sneakers (size 8) for under $70 that can arrive by Friday."
    print("\n=== Task B: Shipping Deadline ===")
    print("Query:", query2)
    response2 = await agent.respond(query2)
    print("Response:", response2)

    # Task C: Competitor Price Comparison
    query3 = "I found a 'casual denim jacket' at $80 on SiteA. Any better deals?"
    print("\n=== Task C: Price Comparison ===")
    print("Query:", query3)
    response3 = await agent.respond(query3)
    print("Response:", response3)

    # Task D: Returns & Policies
    query4 = "I want to buy a cocktail dress from SiteB, but only if returns are hassle-free. Do they accept returns?"
    print("\n=== Task D: Return Policy ===")
    print("Query:", query4)
    response4 = await agent.respond(query4)
    print("Response:", response4)

    # Task E: Multi-Tool Combined Query
    query5 = """I'm looking for a black leather handbag under $100 that:
    1. Can be delivered within 5 days
    2. Has a good return policy
    3. Might have available discounts
    4. Is the best price compared to other stores"""
    print("\n=== Task E: Multi-Tool Query ===")
    print("Query:", query5)
    response5 = await agent.respond(query5)
    print("Response:", response5)

if __name__ == "__main__":
    asyncio.run(main())