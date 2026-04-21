"""
-----------------------------------------------------------------------
ASSIGNMENT 14A: Object practice
-----------------------------------------------------------------------
[X] 1. Header Docstring included.
[X] 2. Define a class using PascalCase.
[X] 3. Use __init__ with private attributes.
[X] 4. Write Setters and Getters.
[X] 5. Write a summary function.
[X] 6. Instantiate two objects and print summaries.
-----------------------------------------------------------------------
Name: Neal McCool
Date: 2026-04-20
"""
class Guitar:
    def __init__(self, brand, model, color, wood, price):
        self.__brand = brand
        self.__model = model
        self.__color = color
        self.__wood = wood
        self.__price = price

# --- Getters ---
    def get_brand(self):
        return self.__brand

    def get_model(self):
        return self.__model

    def get_color(self):
        return self.__color

    def get_wood(self):
        return self.__wood

    def get_price(self):
        return self.__price

# --- Setters ---
    def set_brand(self, brand):
        self.__brand = brand

    def set_model(self, model):
        self.__model = model

    def set_color(self, color):
        self.__color = color

    def set_wood(self, wood):
        self.__wood = wood

    def set_price(self, price):
        self.__price = price

# --- Summary ---
    def get_summary(self):
        return (f"{self.__brand} {self.__model} | "
                f"Color: {self.__color} | "
                f"Wood: {self.__wood} | "
                f"Price: ${self.__price:.2f}")


# --- Objects ---
guitar1 = Guitar("Jackson", "Rhoads V", "Black", "Poplar", 2499.99)
guitar2 = Guitar("ESP", "Horizon FR-7", "EmeraldBurst", "Alder", 3299.99)

# --- Using Setter ---
guitar1.set_price(2449.99)

# --- Showing Summary ---
print(guitar1.get_summary())
print(guitar2.get_summary())