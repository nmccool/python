"""
ASSIGNMENT 9B: SPRINT 3 - REVIEW BOARD
Project: Rough Draught v1.1
Developer: Neal McCool
Date: 2026-03-30
"""
# --- Updated for Sprint 4 ---
import datetime
entry_id = 1

# GLOBAL CONSTANTS (Brewery Rules)
BEER_LOG = "beer_log.txt"

# --- Updated for Sprint 3 ---
STYLES = ("IPA", "Lager", "Pilsner", "Porter", "Stout", 
          "Wheat", "Belgian / Farmhouse (Saison, Dubbel, Tripel)", 
          "Sour", "Barleywine", "Other")
STRENGTHS = ("Session", "Standard", "Imperial")
COUNTRIES = ("United States", "Germany", "Belgium", 
             "United Kingdom", "Ireland", "Canada", 
             "Mexico", "Other")

def get_user_info():
    """Asks for user's name and location."""
    name = input("Enter your name: ").strip().title()
    location = input("Enter your City, State: ").strip().title()
    return name, location

""" TODO still need to add crash prevention to all inputs"""
def collect_beer_data(rating=0):
    """Collects beer entry data."""
    
    # --- Name of beer
    beer_name = input("Beer Name: ").strip().title()

    # --- Name of brewery
    brewery = input("Brewery: ").strip().title()

    # --- Price paid
    price = float(input("Price: $"))

    # --- Alcohol amount
    abv = float(input("ABV (%): "))
    
    # Style, strength, and country sections still needed
    
    # Rating
    while True:
        user_rating = input("Rate beer 1-5 or press 'ENTER' to skip: ").strip()
        if user_rating == "":
            break
        elif user_rating.isdigit() and 1 <= int(user_rating) <= 5:
            rating = int(user_rating)
            break
        else:
            print("Invalid selection. Please enter a rating 1-5.")
    
    # Dictionary
    return {
        "beer_name": beer_name,
        "brewery": brewery,
        "price": price,
        "abv": abv,
        "style": None,
        "strength": None,
        "country": None,
        "rating": rating,
    }

# --- Calculated Rating
def calculate_rating(beer_entry):
    return beer_entry["rating"]

# --- Saving data
def save_data_and_label(name, location, beer_entry, rating_result):
    """Prints the beer entry summary."""
    global entry_id
    print("\n--- ROUGH DRAUGHT ENTRY ---")
    print(f"User: {name}")
    print(f"Location: {location}")
    print(f"Beer: {beer_entry['beer_name']}")
    print(f"Brewery: {beer_entry['brewery']}")
    print(f"Price: ${beer_entry['price']:.2f}")
    print(f"ABV: {beer_entry['abv']:.1f}%")
    print(f"Rating: {rating_result}")   

# --- Datetime module ---        
    current_time = datetime.datetime.now()

# --- Store Datetime ---
    timestamp = current_time.strftime("%Y-%m-%d %H:%M:%S")
    
# --- Log entry ---
    log_entry = "*" * 50 + "\n"
    log_entry += f"BEER ENTRY {entry_id}\n"
    log_entry += f"Timestamp: {timestamp}\n"
    log_entry += f"User: {name}\n"
    log_entry += f"Location: {location}\n"
    log_entry += f"Beer: {beer_entry['beer_name']}\n"
    log_entry += f"Brewery: {beer_entry['brewery']}\n"
    log_entry += f"Price: ${beer_entry['price']:.2f}\n"
    log_entry += f"ABV: {beer_entry['abv']:.1f}%\n"
    log_entry += f"Style: {beer_entry['style']}\n"
    log_entry += f"Strength: {beer_entry['strength']}\n"
    log_entry += f"Country: {beer_entry['country']}\n"
    log_entry += f"Rating: {beer_entry['rating']}\n"
    log_entry += "*" * 50 + "\n"
    log_entry += "\n"

# --- With open and beer_log ---         
    with open(BEER_LOG, "a") as file:
        file.write(log_entry)

#  TODO Entry counter needs to be persistent           
    entry_id += 1
    print("Your beer entry has been saved.")

def main():
    # 1. Identity Phase
    name, location = get_user_info()

    # 2. Data Collection Phase
    beer_entry = collect_beer_data()

    # 3. Calculation Phase
    rating_result = calculate_rating(beer_entry)

    # 4. Handoff Phase
    save_data_and_label(
        name=name,
        location=location,
        beer_entry=beer_entry,
        rating_result=rating_result
    )

main()