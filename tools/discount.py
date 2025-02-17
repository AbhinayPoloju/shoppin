import asyncio
from typing import Dict

DISCOUNTS = {
    "SAVE10": 10,
    "BEN10": 10,
    "SILKY69": 69, #try this one, highest discount you can get
}

async def discount_checker(base_price: float, promo_code: str) -> Dict:
  
    await asyncio.sleep(1)  # adding some delay 

    # validate inputs
    if base_price < 0:
        return {"error": "bro, you came for shoppin not robbery"}
    
    promo_code = promo_code.strip().upper()  # normalizing promo code
    discount_percentage = DISCOUNTS.get(promo_code, 0)  # get discount percentage
    
    discount_amount = round((base_price * discount_percentage) / 100, 2)  # calculate discount amount
    final_price = round(base_price - discount_amount, 2)  # apply discount

    return {
        "code": promo_code,
        "base_price": base_price,
        "discount_percentage": discount_percentage,
        "discount_amount": discount_amount, 
        "final_price": final_price,
    }
