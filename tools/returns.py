import asyncio

async def return_policy_checker(site):
    """Check return policies for specific sites."""
    await asyncio.sleep(1)  # Simulate asynchronous behavior
    policies = {
        "SiteA": "30-day hassle-free returns",
        "SiteB": "14-day returns with receipt and $10 fee",
        "SiteC": "No returns on sale items",
    }
    return {"site": site, "policy": policies.get(site, "Policy not found")}