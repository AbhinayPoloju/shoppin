import asyncio
import random

async def competitor_price_comparison(product_name: str):
    """Compare prices across competitors with a fun twist!"""
    
    await asyncio.sleep(random.uniform(0.5, 1.5))  # adding some delay to help you 

    # just randomly added some data to display something for you when you call this func
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
    
    # normalizing the name 
    product_name = product_name.strip().lower()
    
    # getting the product price
    prices = product_prices.get(product_name, [])

    # this is not shoppin website, you don't have so may options, choose from what I added bro
    if not prices:
        return {
            "message": f"oops! no results found for '{product_name}'. this is not shoppin website, you don't have so may options, choose from what I added in code bro"
        }
    
    # adding some fluctuations to keep it realistic 
    for price_entry in prices:
        fluctuation = random.uniform(-0.1, 0.1)  # randomly adjusting price by ±10%
        price_entry["price"] = round(price_entry["price"] * (1 + fluctuation), 2)
    
    return {
        "product": product_name.title(),
        "competitor_prices": prices,
        "best_deal": min(prices, key=lambda x: x["price"])  # finding you the best deal, the cheapest one, I know you are not rich
    }
