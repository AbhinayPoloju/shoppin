import aiohttp
import asyncio
import random
from typing import List, Dict, Optional
from tools.discount import discount_checker  # Import the discount_checker function

async def ecommerce_search_aggregator(
    product_name: str,
    color: Optional[str] = None,
    price_range: Optional[float] = None,
    size: Optional[str] = None,
    sort_by: Optional[str] = "price",
    limit: Optional[int] = 5,
    promo_code: Optional[str] = None,  
) -> List[Dict]:
    
    async with aiohttp.ClientSession() as session:
        # mock api calls 
        tasks = [
            _mock_api_call(session, "SiteA", product_name, color, price_range, size),
            _mock_api_call(session, "SiteB", product_name, color, price_range, size),
            _mock_api_call(session, "SiteC", product_name, color, price_range, size),
        ]
        results = await asyncio.gather(*tasks)
    
    # combining and filtering the results
    valid_results = [result for sublist in results for result in sublist if "error" not in result]
    if not valid_results:
        return {"error": "No products found matching the criteria."}
    
    # Sort results
    if sort_by == "price":
        valid_results.sort(key=lambda x: x["price"])
    elif sort_by == "rating":
        valid_results.sort(key=lambda x: x.get("rating", 0), reverse=True)
    elif sort_by == "popularity":
        valid_results.sort(key=lambda x: x.get("popularity", 0), reverse=True)
    
    # Limit results
    valid_results = valid_results[:limit]
    
    # Apply promo code to the best product (first in the sorted list)
    if promo_code:
        best_product = valid_results[0]
        discount_result = await discount_checker(best_product["price"], promo_code)
        best_product.update({
            "promo_code": discount_result["code"],
            "discount": discount_result["discount"],
            "final_price": discount_result["final_price"],
        })
    
    return valid_results

async def _mock_api_call(
    session: aiohttp.ClientSession,
    site: str,
    product_name: str,
    color: Optional[str],
    price_range: Optional[float],
    size: Optional[str],
) -> List[Dict]:
    
    await asyncio.sleep(1)  # Simulate network latency
    
    # Mock product database
    products = [
        # Floral Skirts
        {"name": "floral skirt", "color": "blue", "price": 35, "size": "S", "in_stock": True, "site": site, "rating": 4.5, "popularity": 80, "promo_available": True},
        {"name": "floral skirt", "color": "red", "price": 45, "size": "S", "in_stock": False, "site": site, "rating": 4.0, "popularity": 70, "promo_available": False},
        {"name": "floral skirt", "color": "green", "price": 40, "size": "M", "in_stock": True, "site": site, "rating": 4.2, "popularity": 75, "promo_available": True},
        
        # White Sneakers
        {"name": "white sneakers", "color": "white", "price": 65, "size": "8", "in_stock": True, "site": site, "rating": 4.8, "popularity": 90, "promo_available": True},
        {"name": "white sneakers", "color": "white", "price": 70, "size": "9", "in_stock": True, "site": site, "rating": 4.7, "popularity": 85, "promo_available": False},
        
        # Casual Denim Jackets
        {"name": "casual denim jacket", "color": "blue", "price": 80, "size": "M", "in_stock": True, "site": site, "rating": 4.6, "popularity": 88, "promo_available": True},
        {"name": "casual denim jacket", "color": "black", "price": 90, "size": "L", "in_stock": True, "site": site, "rating": 4.4, "popularity": 82, "promo_available": False},
        
        # Cocktail Dresses
        {"name": "cocktail dress", "color": "black", "price": 120, "size": "S", "in_stock": True, "site": site, "rating": 4.9, "popularity": 95, "promo_available": True},
        {"name": "cocktail dress", "color": "red", "price": 110, "size": "M", "in_stock": True, "site": site, "rating": 4.8, "popularity": 92, "promo_available": False},
        
        # Black Leather Handbags
        {"name": "black leather handbag", "color": "black", "price": 150, "size": "One Size", "in_stock": True, "site": site, "rating": 4.7, "popularity": 89, "promo_available": True},
        {"name": "black leather handbag", "color": "black", "price": 140, "size": "One Size", "in_stock": True, "site": site, "rating": 4.6, "popularity": 87, "promo_available": False},
    ]
    
    # adding random price variations
    for product in products:
        base_price = product["price"]
        # generating random price variations upto 10%
        price_variation = random.uniform(-0.1, 0.1) * base_price
        product["price"] = round(base_price + price_variation, 2)
    
    # filtering products based on the criteria
    filtered_products = []
    for product in products:
        if (product["name"].lower() == product_name.lower() and
            (color is None or product["color"].lower() == color.lower()) and
            (price_range is None or product["price"] <= price_range) and
            (size is None or product["size"].lower() == size.lower())):
            filtered_products.append(product)
    
    if not filtered_products:
        return [{"error": f"oops,no products found on {site}.btw, how you doin'? better choose the floral skirt/white sneakers/casual denim jacket/cocktail dress or black leather handbag,i don't want to add so many items bro.this is just an assignment."}]
    return filtered_products