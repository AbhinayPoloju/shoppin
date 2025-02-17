from datetime import datetime, timedelta
import random

async def shipping_time_estimator(product_name, size, user_location, delivery_date):
    
    #estimating the delivery time
    delivery_date = datetime.strptime(delivery_date, "%Y-%m-%d")
    today = datetime.today()
    if delivery_date < today:
        return {"error": "delivery will come today, watch rick and morty until then"}
    
    shipping_details = {
        "product_name": product_name,
        "size": size,
        "user_location": user_location,
        "delivery_date": delivery_date.strftime("%Y-%m-%d"),
        "feasible": True,
        "cost": round(random.uniform(5.99, 15.99), 2),
        "estimated_delivery": (today + timedelta(days=random.randint(2, 7))).strftime("%Y-%m-%d"),
    }
    return shipping_details