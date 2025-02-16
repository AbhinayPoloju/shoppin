import asyncio
from random import randint

async def competitor_price_comparison(product_name):
    """Compare prices across competitors based on the product name."""
    await asyncio.sleep(1)  # Simulate asynchronous behavior (e.g., API call delay)
    
    # Simulate a database or API response with product prices
    product_prices = {
        "floral skirt": [
            {"site": "SiteA", "price": 35},
            {"site": "SiteB", "price": 32},
            {"site": "SiteC", "price": 38},
        ],
        "white sneakers": [
            {"site": "SiteA", "price": 70},
            {"site": "SiteB", "price": 65},
            {"site": "SiteC", "price": 75},
        ],
        "casual denim jacket": [
            {"site": "SiteA", "price": 80},
            {"site": "SiteB", "price": 75},
            {"site": "SiteC", "price": 85},
        ],
        "cocktail dress": [
            {"site": "SiteA", "price": 120},
            {"site": "SiteB", "price": 110},
            {"site": "SiteC", "price": 130},
        ],
        "black leather handbag": [
            {"site": "SiteA", "price": 150},
            {"site": "SiteB", "price": 140},
            {"site": "SiteC", "price": 160},
        ],
    }
    
    # Fetch prices for the given product name
    prices = product_prices.get(product_name.lower(), [])
    
    # If the product is not found, return an empty list or a default response
    if not prices:
        return [{"site": "No results", "price": 0}]
    
    # Add some variability to simulate real-world price fluctuations
    for price_entry in prices:
        price_entry["price"] += randint(-5, 5)  # Randomly adjust prices by +/- $5
    
    return prices