import asyncio

async def competitor_price_comparison(product_name, price):
    """Compare prices across competitors."""
    await asyncio.sleep(1)  # Simulate asynchronous behavior
    prices = [
        {"site": "SiteA", "price": 80},
        {"site": "SiteB", "price": 75},
        {"site": "SiteC", "price": 85},
    ]
    better_deals = [deal for deal in prices if deal["price"] < price]
    return better_deals