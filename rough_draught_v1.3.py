

"""
ASSIGNMENT 12B: SPRINT 5 - REVIEW BOARD
Project: Rough Draught v1.3
Developer: Neal McCool
Date: 2026-04-13
"""
import datetime


# --- GLOBAL CONSTANTS (Brewery Rules) ---
BEER_FILE = "beer_file.txt"
DATA_FILE = "entry_history.txt"
HUMAN_REPORT = "human_report.txt"

# --- TODO replace location with 'where purchased' more relevant than city/state.
#  --- Asks for user's name and location ---
def get_user_info():
    name = input("Enter your name: ").strip().title()
    location = input("Enter your City, State: ").strip().title()
    return name, location

# --- Reads beer classes from external file into a dictionary ---
def load_beer_file():
    beer_dictionary = {}

    try:
        with open(BEER_FILE, "r") as file:
            for line in file:
                line = line.strip()
                category, items = line.split(":")
                beer_dictionary[category] = [item.strip() for item in items.split(",")]
    except FileNotFoundError:
        print("Error! beer_file.txt missing!")

    return beer_dictionary

# --- Collects beer entry data ---
def collect_beer_data(beer_dictionary, rating=0):
    styles = beer_dictionary["Styles"]
    strengths = beer_dictionary["Strengths"]
    countries = beer_dictionary["Countries"]
    
# --- Name of beer ---
    beer_name = input("Beer Name: ").strip().title()

# --- Name of brewery ---
    brewery = input("Brewery: ").strip().title()

# --- Price paid ---
    price = float(input("Price: $"))

# --- Alcohol amount ---
    abv = float(input("ABV (%): "))

# --- Style ---
    print("\nSelect a Style:")
    for index, style in enumerate(styles, start=1):
        print(f"{index}. {style}")
    style_choice = int(input("Enter style number: "))
    style = styles[style_choice - 1]

# --- Strength ---
    print("\nSelect a Strength:")
    for index, strength in enumerate(strengths, start=1):
        print(f"{index}. {strength}")
    strength_choice = int(input("Enter strength number: "))
    strength = strengths[strength_choice - 1]

# --- Country ---
    print("\nSelect a Country:")
    for index, country in enumerate(countries, start=1):
        print(f"{index}. {country}")
    country_choice = int(input("Enter country number: "))
    country = countries[country_choice - 1]

# TODO add "Tasting Notes" section

# --- Rating ---
    while True:
        user_rating = input("Rate beer 1-5 or press 'ENTER' to skip: ").strip()
        if user_rating == "":
            break
        elif user_rating.isdigit() and 1 <= int(user_rating) <= 5:
            rating = int(user_rating)
            break
        else:
            print("Invalid selection. Please enter a rating 1-5.")


# --- Dictionary ---
    return {
        "beer_name": beer_name,
        "brewery": brewery,
        "price": price,
        "abv": abv,
        "style": style,
        "strength": strength,
        "country": country,
        "rating": rating,
    }

# --- Calculated Rating ---
def calculate_rating(beer_entry):
    return beer_entry["rating"]

# --- Saving data ---
def save_data_and_label(name, location, beer_entry, rating_result):
    print("-" * 50)
    print("ROUGH DRAUGHT ENTRY")
    print("-" * 50)
    print(f"User: {name}")
    print(f"Location: {location}")
    print(f"Beer: {beer_entry['beer_name']}")
    print(f"Brewery: {beer_entry['brewery']}")
    print(f"Price: ${beer_entry['price']:.2f}")
    print(f"ABV: {beer_entry['abv']:.1f}%")
    print(f"Rating: {rating_result}")
    print("-" * 50)

    current_time = datetime.datetime.now()
    timestamp = current_time.strftime("%Y-%m-%d %H:%M:%S")

# --- Raw Data File (Append) ---
    with open(DATA_FILE, "a") as file:
        file.write(
            f"{timestamp} | "
            f"{name} | "
            f"{location} | "
            f"{beer_entry['beer_name']} | "
            f"{beer_entry['brewery']} | "
            f"{beer_entry['price']:.2f} | "
            f"{beer_entry['abv']:.1f} | "
            f"{beer_entry['style']} | "
            f"{beer_entry['strength']} | "
            f"{beer_entry['country']} | "
            f"{rating_result}\n"
        )
# TODO add code to display rating in Human Report as star emoji instead of number
# --- Human Report File (Write) ---
    with open(HUMAN_REPORT, "w") as file:
        file.write("-" * 50 + "\n")
        file.write("ROUGH DRAUGHT ENTRY")
        file.write("-" * 50 + "\n")
        file.write(f"Timestamp: {timestamp}\n")
        file.write(f"User: {name}\n")
        file.write(f"Location: {location}\n")
        file.write(f"Beer: {beer_entry['beer_name']}\n")
        file.write(f"Brewery: {beer_entry['brewery']}\n")
        file.write(f"Price: ${beer_entry['price']:.2f}\n")
        file.write(f"ABV: {beer_entry['abv']:.1f}%\n")
        file.write(f"Style: {beer_entry['style']}\n")
        file.write(f"Strength: {beer_entry['strength']}\n")
        file.write(f"Country: {beer_entry['country']}\n")
        file.write(f"Rating: {rating_result}\n")

    print(f"Success! Your entry is saved.")

# --- Review stored entries ---
def review_entry_history():
    try:
        with open(DATA_FILE, "r") as file:
            print("-" * 50)
            print("\nENTRY HISTORY REVIEW")
            print("-" * 50)
            for line in file:
                print(line.strip())
    except FileNotFoundError:
        print("Error: entry history file not found.")

def main():
# --- Load external beer info ---
    beer_dictionary = load_beer_file()

    if not beer_dictionary:
        return

# --- Get User Info ---
    name, location = get_user_info()

# --- Data Collection ---
    beer_entry = collect_beer_data(beer_dictionary)

# --- Rating Calculation ---
    rating_result = calculate_rating(beer_entry)

# --- Handoff ---
    save_data_and_label(
        name=name,
        location=location,
        beer_entry=beer_entry,
        rating_result=rating_result
    )

# --- Review Entry ---
    review_entry_history()

main()