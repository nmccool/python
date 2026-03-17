"""
-----------------------------------------------------------------------
ASSIGNMENT 9A: THE SMOOTHIE SPRINT
-----------------------------------------------------------------------
[X] 1. Header Docstring included.
[X] 2. Global Constants BASES and FRUITS defined as Tuples.
[X] 3. Professional function get_price(size) returns a float.
[X] 4. Professional function blend(size, base, fruit, scoops) for output.
[X] 5. main() function handles try/except for scoops (int).
[X] 6. main() calls both functions correctly.
-----------------------------------------------------------------------

Name: Neal McCool
Date: 2026-03-16
"""

# GLOBAL CONSTANTS (The Pantry)
BASES = ("Water", "Apple Juice", "Orange Juice", "Milk")
FRUITS = ("Strawberry", "Banana", "Mango", "Blueberry")
SIZE_PRICE = {
    "S": ("Small", 3.00),
    "SM": ("Small", 3.00),
    "SMALL": ("Small", 3.00),

    "M": ("Medium", 4.00),
    "MD": ("Medium", 4.00),
    "MED": ("Medium", 4.00),
    "MEDIUM": ("Medium", 4.00),

    "L": ("Large", 5.00),
    "LG": ("Large", 5.00),
    "LAR": ("Large", 5.00),
    "LARGE": ("Large", 5.00)
}
print("-" * 50)


def get_price(size):
    return SIZE_PRICE.get(size, (None, 0.00))

def blend(size, base, fruit, scoops):
    print("-" * 50)
    print("--- Smoothie Order ---")
    print(f"Size: {size}")
    print(f"Base: {base}")
    print(f"Fruit: {fruit} x ({scoops} scoops)")


def main():
    print("Welcome to McCool's Smoothie Bar!")

    while True:
        choose_size = input("What size would you like? (Small, Medium, or Large): ").upper().strip()
        if choose_size in SIZE_PRICE:
            print(f"{choose_size} = ${get_price(choose_size)[1]:.2f}")
            break
        else:
            print("Invalid size entry. Please choose a size.")

    while True:
        choose_base = input("Select Base: (Water, Apple Juice, Orange Juice, or Milk) ").title().strip()
        if choose_base in ("Water", "Apple Juice", "Apple", "Orange Juice", "Orange", "Milk"):
            break
        else:
            print("Invalid entry. Please select a base.")

    while True:
        choose_fruit = input("Select Fruit: Strawberry, Banana, Mango, or Blueberry: ").title().strip()
        if choose_fruit in FRUITS:
            break
        else:
            print("Invalid entry. Please select a fruit.")

    try:
        choose_scoops = int(input("How many scoops of fruit? ($1.00 each): "))
        scoop_cost = choose_scoops * 1.00
        print(f"{choose_scoops} scoops = ${scoop_cost:.2f}")
    except ValueError:
        print("Invalid entry. Defaulting to 0.")
        choose_scoops = 0
        scoop_cost = 0.00

    total = get_price(choose_size)[1] + (choose_scoops * 1.00)
    
    blend(choose_size, choose_base, choose_fruit, choose_scoops)

    print(f"Total: ${total:.2f}")

main()
print("-" * 50)