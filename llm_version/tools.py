# tools.py

def ecommerce_search_aggregator(product_name, color, price_range, size):
    """Mock function to simulate searching across e-commerce platforms."""
    # Example mock data
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
    
    filtered_products = [p for p in products if p["price"] <= price_range and p["size"] == size and p["color"] == color]
    return filtered_products

def shipping_time_estimator(product_id, user_location, delivery_date):
    """Mock function to simulate shipping time estimation."""
    # Example mock data
    return {
        "feasible": True,
        "cost": 5.99,
        "estimated_delivery": delivery_date,
    }

def discount_checker(base_price, promo_code):
    """Mock function to simulate discount application."""
    discounts = {
        "SAVE10": 0.10,
        "FASHION20": 0.20,
    }
    discount = discounts.get(promo_code, 0)
    final_price = base_price * (1 - discount)
    return final_price

def competitor_price_comparison(product_name):
    """Mock function to simulate competitor price comparison."""
    # Example mock data
    return {
        "SiteA": 80,
        "SiteB": 75,
        "SiteC": 85,
    }

def return_policy_checker(site_name):
    """Mock function to simulate return policy lookup."""
    policies = {
        "SiteA": "30-day return policy, hassle-free.",
        "SiteB": "14-day return policy, restocking fee applies.",
    }
    return policies.get(site_name, "Return policy not found.") 