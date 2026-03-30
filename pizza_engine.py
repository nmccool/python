"""
-----------------------------------------------------------------------
ASSIGNMENT 10A: THE RESILIENT PIZZA ENGINE
-----------------------------------------------------------------------
[X] 1. Header Docstring included.
[X] 2. Global constant TOPPINGS defined as a Tuple in ALL_CAPS.
[X] 3. Function 'make_pizza' defines 4 specific parameters.
[X] 4. 'make_pizza' uses a DEFAULT value for is_delivery.
[X] 5. main() displays the Global Pantry list to the user.
[X] 6. main() calls the function using KEYWORD ARGUMENTS.
-----------------------------------------------------------------------
NAME: NEAL MCCOOL
DATE: 2026-03-30

"""
#2 --- GLOBAL CONSTANT(S) ---
SIZES= ("Small", "Medium", "Large", "XL")
CRUSTS = ("Thin", "Hand Tossed", "Deep Dish")
TOPPINGS = ("Pepperoni", "Sausage", "Chicken", "Bacon", "Mushrooms", "Olives", "Green Peppers", "Pineapple")

#3&4 --- 4 parameters and a default)
def make_pizza (size, crust, topping, is_delivery=False):

    size = size.strip().title()
    crust = crust.strip().title()
    topping = topping.strip().title()

    print(f"Size: {size}")
    print(f"Crust: {crust}")
    print(f"Topping: {topping}")

    if is_delivery:
        print("*** Delivery ***")
    else:
        print("*** Carry Out ***")

#5 --- Main displays Global Pantry ---

def main():
    print("-" * 50)
    print("Welcome to McCool's Pizzeria")
    print("-" * 50)

    print("What size pizza would you like?") 
    while True:
        size = input(" | ".join (SIZES)+": ").strip().title()
        if size in SIZES:
            break
        else:
            print("Invalid selection. Please choose a size.")
    print("\nWhat type of crust would you like?")
    while True:
        crust = input(" | ".join (CRUSTS)+": ").strip().title()
        if crust in CRUSTS:
            break
        else:
            print("Invalid selection. Please choose a crust.")
    print("\nWhat topping would you like?")        
    while True:
        topping = input(" | ".join (TOPPINGS)+": ").strip().title()
        if topping in TOPPINGS:
            break
        else:
            print("Invalid selection.  Please choose a topping.")
    is_delivery = input("\nWould like delivery? (yes/no) ").strip().lower() == "yes"

#6 --- KEYWORD ARGUMENTS ---
    print("\n--- PIZZA ORDER ---")
    make_pizza(size = size, crust = crust, topping = topping, is_delivery = is_delivery)

main()