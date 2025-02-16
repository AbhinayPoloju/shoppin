import re
from datetime import datetime, timedelta

def extract_parameters(query):
    """
    Extract parameters from the user query.
    """
    params = {}
    
    # Extract product name
    product_match = re.search(r"floral skirt|white sneakers|casual denim jacket|cocktail dress|black leather handbag", query, re.IGNORECASE)
    if product_match:
        params["product_name"] = product_match.group(0).lower()
    
    # Extract price range
    price_match = re.search(r"under \$(\d+)", query)
    if price_match:
        params["price_range"] = float(price_match.group(1))
    
    # Extract size
    size_match = re.search(r"size (\w+)", query, re.IGNORECASE)
    if size_match:
        params["size"] = size_match.group(1).upper()
    
    # Extract promo code
    promo_match = re.search(r"discount code (\w+)", query, re.IGNORECASE)
    if promo_match:
        params["promo_code"] = promo_match.group(1).upper()
    
    # Extract site
    site_match = re.search(r"Site\w+", query)
    if site_match:
        params["site"] = site_match.group(0)
    
    # Extract delivery date (e.g., "by Friday")
    date_match = re.search(r"by (\w+)", query, re.IGNORECASE)
    if date_match:
        day_of_week = date_match.group(1).lower()
        params["delivery_date"] = convert_day_to_date(day_of_week)
    
    return params

def convert_day_to_date(day_of_week):
    """
    Convert a day of the week (e.g., "Friday") into a valid date (YYYY-MM-DD).
    """
    days = {
        "monday": 0,
        "tuesday": 1,
        "wednesday": 2,
        "thursday": 3,
        "friday": 4,
        "saturday": 5,
        "sunday": 6,
    }
    
    today = datetime.today()
    target_day = days.get(day_of_week)
    
    if target_day is None:
        raise ValueError(f"Invalid day of the week: {day_of_week}")
    
    # Calculate the date of the next occurrence of the target day
    days_until_target = (target_day - today.weekday() + 7) % 7
    target_date = today + timedelta(days=days_until_target)
    
    return target_date.strftime("%Y-%m-%d")