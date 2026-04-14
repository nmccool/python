"""
-----------------------------------------------------------------------
ASSIGNMENT 12A: THE CONFIGURABLE MENU & AUDITOR
-----------------------------------------------------------------------
[X] 1. Header Docstring included.
[X] 2. PHASE 1: External menu_config.txt file created in workspace.
[X] 3. Program reads and parses the .txt file into a Dictionary.
[X] 4. PHASE 2: break the dictionary into individual variables.
[X] 6. Print each category and its details
[X] 7. try/except used to prevent crashes on FileNotFoundError.
-----------------------------------------------------------------------
Name: Neal McCool
Date: 2026-04-13
"""

#2 --- Phase 1 ---
guitar_menu_dictionary = {}

#3&7 --- Read txt ---
try:
    with open("guitar_menu_config.txt", "r") as file:
        for line in file:
            line = line.strip()
            category, items = line.split(":")
            guitar_menu_dictionary[category] = [item.strip() for item in items.split(",")]



    #4 --- Break up Dictionary ---
    brands = guitar_menu_dictionary["Brands"]
    types = guitar_menu_dictionary["Types"]
    woods = guitar_menu_dictionary["Woods"]
    price_range = guitar_menu_dictionary["Price Range"]

    #5 --- Number 5 is missing in the Doc String ;) ---

    #6 --- Print Category ---
    print("-" * 50)
    print("Welcome to McCool's Guitar Shop")
    print("-" * 50)
    print("We sell:")
    print("\nBrands: ")
    for brand in brands:
        print(f"- {brand}")
    print("\nTypes: ")
    for type in types:
        print(f"- {type}")
    print("\nWoods: ")
    for wood in woods:
        print(f"- {wood}")
    print("\nPrice Range: ")
    for price in price_range:
        print(f"- {price}")
    print("-" * 50)    

except FileNotFoundError:
    print("Error! Correct File Not Found.")