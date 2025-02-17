# main.py

import asyncio
from agent.agent import ShoppingAgent

async def main():
    agent = ShoppingAgent()
    #wrote these queries to demonstrate the tasks in assignment, haven't used any llm's/nlp for returning responses. just returning json, i like this guy jason
    # Task A: Basic Item Search + Price Constraint
    query1 = "Find a floral skirt under $45 in size S. Is it in stock, and can I apply a discount code 'SILKY69'?"
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
    query3 = "I found a 'casual denim jacket' at $80 on Amazon. Any better deals?"
    print("\n=== Task C: Price Comparison ===")
    print("Query:", query3)
    response3 = await agent.respond(query3)
    print("Response:", response3)

    # Task D: Returns & Policies
    query4 = "I want to buy a cocktail dress from Flipkart, but only if returns are hassle-free. Do they accept returns?"
    print("\n=== Task D: Return Policy ===")
    print("Query:", query4)
    response4 = await agent.respond(query4)
    print("Response:", response4)

    # Task E: Multi-Tool Combined Query
    #activates all the intents in this query

    query5 = """
     Find a floral skirt under $40 in size S that can arrive by Friday.Check if there are any better deals.Is it in stock, and can I apply a discount code 'SAVE10'?Returns should be hassle-free. Do they accept returns? 
     """
    print("\n=== Task E: Multi-Tool Query ===")
    print("Query:", query5)
    response5 = await agent.respond(query5)
    print("Response:", response5)
    
#if you need more advanced version of this assignment with added features, let me know, I will implement that
if __name__ == "__main__":
    asyncio.run(main())
    