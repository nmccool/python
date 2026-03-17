"""
ASSIGNMENT 9B: SPRINT 2 - FUNCTIONAL STUBS
Project: Rough Draught v1.0
Developer: Neal McCool
Date: 2026-03-16
"""

# ---I'm basically reverse engineering Monty's Code Stub to fit my 

# GLOBAL CONSTANTS (Pantry Rules)
BEER_LOG = "beer_log.txt"

def get_user_info():
    """Asks for user's name"""
    # TODO: Ask for user's name and city/state
    return "Neal McCool", "Woodstock, IL"

def collect_beer_data():
    """Collects beer entry data."""
    # TODO: Capture beer info, outline style, strength, country, rating maps
    style = 5
    strength = 3
    country = 1
    rating = 5
    return {
        "beer_name": "Old Rasputin",
        "brewery": "North Coast Brewing Co.",
        "price": 10.99,
        "abv": 9.0,
        "style": style,
        "strength": strength,
        "country": country,
        "rating": rating,
    }

def calculate_rating(beer_entry):
    """Calculates rating summary based on stars awarded and 'buy again?'."""
    # TODO: Load ratings from beer_log.txt
    return "Top Shelf!"

def save_data_and_label(name, beer_entry, rating_result):
    """Appends to beer_log.txt and prints the human-readable label."""
    # TODO: Write raw data for computer and readable results for user
    pass

def main():
    # 1. Identity Phase
    name, location = get_user_info()
    print(f"User: {name} | Location: {location}")

    # 2. Data Collection Phase
    beer_entry = collect_beer_data()

    # 3. Calculation Phase
    rating_result = calculate_rating(beer_entry)

    # 4. Handoff Phase
    save_data_and_label(name, beer_entry, rating_result)

main()