import asyncio
import random

async def return_policy_checker(site: str):
    # Simulate a realistic delay
    await asyncio.sleep(random.uniform(0.5, 1.5))
    
    # Define detailed return policies for each site
    policies = {
        "Amazon": {
            "policy": "30-day free returns! No questions asked, just pure refund joy!",
            "conditions": [
                "Items must be in original condition and packaging.",
                "Some items like electronics may have a 15-day return window.",
                "Free return shipping for most items."
            ]
        },
        "Flipkart": {
            "policy": "14-day returns allowed, but only with a receipt... and a $10 'oops' fee!",
            "conditions": [
                "Product should not be worn out or damaged.",
                "Original tags and packaging must be intact.",
                "Certain items like innerwear and cosmetics are non-returnable."
            ]
        },
        "H&M": {
            "policy": "No returns on sale items! Once it’s yours, it’s yours forever. Choose wisely!",
            "conditions": [
                "Regular items can be returned within 28 days.",
                "Items must be unworn, unwashed, and with original tags.",
                "Receipt or proof of purchase is required."
            ]
        },
    }

    # Get the policy details for the given site
    policy_details = policies.get(site, {
        "policy": f"Oops! No return policy found for {site}. Add this to your regret list.",
        "conditions": []
    })

    return {
        "site": site,
        "policy": policy_details["policy"],
        "conditions": policy_details["conditions"]
    }
