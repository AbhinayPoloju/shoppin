# tools/search.py

import asyncio

async def ecommerce_search_aggregator(product_name, color=None, price_range=None, size=None):
    """Search for products across e-commerce sites with realistic data."""
    products = [
        {"name": "floral skirt", "color": "blue", "price": 35, "size": "S", "in_stock": True, "site": "SiteA"},
        {"name": "floral skirt", "color": "red", "price": 45, "size": "S", "in_stock": False, "site": "SiteB"},
        {"name": "white sneakers", "color": "white", "price": 65, "size": "8", "in_stock": True, "site": "SiteC"},
        {"name": "casual denim jacket", "color": "blue", "price": 80, "size": "M", "in_stock": True, "site": "SiteA"},
        {"name": "cocktail dress", "color": "black", "price": 120, "size": "L", "in_stock": True, "site": "SiteB"},
        {"name": "black leather handbag", "color": "black", "price": 90, "size": "One Size", "in_stock": True, "site": "SiteD"},  # Added product
    ]
    
    results = []
    for product in products:
        if (product["name"] == product_name and
            (color is None or product["color"] == color) and
            (price_range is None or product["price"] <= price_range) and
            (size is None or product["size"] == size)):
            results.append(product)
    
    if not results:
        return {"error": "No products found matching the criteria."}
    return results