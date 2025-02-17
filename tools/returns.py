import asyncio
import random

async def return_policy_checker(site: str):
    
    await asyncio.sleep(random.uniform(0.5, 1.5)) #adding some delay to keep t realistic, we know servers are slow
    
    policies = {
        "SiteA": "30-day hassle-free returns! No questions asked, just pure refund joy!",
        "SiteB": "14-day returns allowed, but only with a receipt... and a $10 'oops' fee!",
        "SiteC": "No returns on sale items! Once it’s yours, it’s yours forever. Choose wisely!",
    }

    # normalizing site name
    site = site.strip().title()

    return {
        "site": site,
        "policy": policies.get(site, f"Oops! No return policy found for {site}. Maybe keep it just in case?"),
    }
