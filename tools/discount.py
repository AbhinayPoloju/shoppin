import asyncio
from typing import Dict

async def discount_checker(base_price: float, promo_code: str) -> Dict:
    
    await asyncio.sleep(1)  # Simulate asynchronous behavior
    discounts = {
        "SAVE10": 0.10,
        "FASHION20": 0.20,
    }
    discount = discounts.get(promo_code, 0)
    final_price = base_price * (1 - discount)
    return {"code": promo_code, "base_price": base_price, "discount": discount, "final_price": final_price}