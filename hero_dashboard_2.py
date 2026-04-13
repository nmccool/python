"""
-----------------------------------------------------------------------
ASSIGNMENT 11A: THE OFFICE HERO DASHBOARD
-----------------------------------------------------------------------
[X] 1. Header Docstring included.
[X] 2. Global constants OFFICE_NAME and TAX_RATE defined in ALL_CAPS.
[X] 3. Function 'process_expenses' returns TWO values (float, string).
[X] 4. main() function uses try/except for numeric price/qty inputs.
[X] 5. main() calls function using KEYWORD ARGUMENTS.
[X] 6. main() correctly unpacks and prints both return values.
-----------------------------------------------------------------------
Name: Neal McCool
Date: 2026-04-11
"""

#2 --- Global Constants ---
OFFICE_NAME = "Rough Draught LLC"
TAX_RATE = 0.05

#3 --- Expense Function ---
def process_expenses(item_name, price, quantity):
    subtotal = price * quantity
    sales_tax = subtotal * TAX_RATE
    grand_total = subtotal + sales_tax

    # --- Summary instead of print ---
    summary = f"--- {OFFICE_NAME} Order ---\n"
    summary += f"Item: {item_name}\n"
    summary += f"Quantity: {quantity}\n"
    summary += f"Subtotal: ${subtotal:.2f}\n"
    summary += f"Sales Tax: ${sales_tax:.2f}\n"
    summary += f"Grand Total: ${grand_total:.2f}\n"

    return grand_total, summary

#4 --- Main Function ---
def main():
    print("-" * 50)
    print("Rough Draught Sales Portal")
    print("-" * 50)

    item_name = input("Enter item name: ")

    try:
        price = float(input("Enter price: $"))
        quantity = int(input("Enter quantity: "))
    except ValueError:
        print("Invalid Entry. Goodbye.")
        return

    #5 --- Keyword Arguments ---
    grand_total, summary = process_expenses(
        item_name=item_name,
        price=price,
        quantity=quantity
    )

    #6 --- Unpack n print ---
    print(summary)

main()