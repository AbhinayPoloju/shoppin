import asyncio

async def discount_checker(base_price, promo_code):
    """Apply discount codes to calculate final prices."""
    await asyncio.sleep(1)  # Simulate asynchronous behavior
    discounts = {
        "SAVE10": 0.10,
        "FASHION20": 0.20,
    }
    discount = discounts.get(promo_code, 0)
    final_price = base_price * (1 - discount)
    return {"base_price": base_price, "discount": discount, "final_price": final_price}