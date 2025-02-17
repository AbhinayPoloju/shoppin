import asyncio
import random

async def return_policy_checker(site: str):
    
    await asyncio.sleep(random.uniform(0.5, 1.5)) #adding some delay to keep t realistic, we know servers are slow
    
    policies = {
        "Amazon": "30-day free returns! No questions asked, just pure refund joy!(wish this can be true)",
        "Flipkart": "14-day returns allowed, but only with a receipt... and a $10 'oops' fee!(charging for return is crime,these guys should be jailed forever)",
        "H&M": "No returns on sale items! Once it’s yours, it’s yours forever. Choose wisely(you got fuc*ed)!",
    }


    return {
        "site": site,
        "policy": policies.get(site, f"oops! no return policy found for {site}. add this to your regret list."),
    }
