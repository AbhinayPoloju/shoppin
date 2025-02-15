# tools/search.py

import aiohttp
import asyncio

async def ecommerce_search_aggregator(product_name, color=None, price_range=None, size=None):
    """Search for products across e-commerce sites using mock APIs."""
    async with aiohttp.ClientSession() as session:
        # Simulate API calls to multiple e-commerce sites
        tasks = [
            _mock_api_call(session, "SiteA", product_name, color, price_range, size),
            _mock_api_call(session, "SiteB", product_name, color, price_range, size),
            _mock_api_call(session, "SiteC", product_name, color, price_range, size),
        ]
        results = await asyncio.gather(*tasks)
    
    # Filter out errors and combine results
    valid_results = [result for result in results if "error" not in result]
    if not valid_results:
        return {"error": "No products found matching the criteria."}
    return valid_results

async def _mock_api_call(session, site, product_name, color, price_range, size):
    """Simulate an API call to an e-commerce site."""
    await asyncio.sleep(1)  # Simulate network latency
    products = [
        {"name": "floral skirt", "color": "blue", "price": 35, "size": "S", "in_stock": True, "site": site},
        {"name": "floral skirt", "color": "red", "price": 45, "size": "S", "in_stock": False, "site": site},
        {"name": "white sneakers", "color": "white", "price": 65, "size": "8", "in_stock": True, "site": site},
    ]
    
    results = []
    for product in products:
        if (product["name"] == product_name and
            (color is None or product["color"] == color) and
            (price_range is None or product["price"] <= price_range) and
            (size is None or product["size"] == size)):
            results.append(product)
    
    if not results:
        return {"error": f"No products found on {site}."}
    return results