"""
-----------------------------------------------------------------------
ASSIGNMENT 6A: TICKET SALES
-----------------------------------------------------------------------
[X] 1. Create a list of 20 seats (numbered 1-20).
[X] 2. Display the list of available seats.
[X] 3. Ask user for a seat number (0 to quit).
[X] 4. Remove the selected seat from the list.
[X] 5. Handle invalid inputs (seat taken or doesn't exist).
[X] 6. Repeat until user quits or seats are empty.
-----------------------------------------------------------------------
Name: Neal McCool
Date: 2026-02-23
Assignment: 6A Lists & Indexes

"""

print("-" * 40)
print("\nWelcome to McCool's Theatre!")
print("Tonight we're going back in time to bring you...") 
print("Back To The Future!\n")

# ---Seat List ---
seats = list(range(1, 21))

while True:

    if not seats:
        print(f"\nSorry. This showing is sold out!")
        break

    print("Available Seats:", seats)

    user_selection = input(f"\nSelect a seat number or enter '0' to Quit: ")
    if user_selection.isdigit():
        selection = int(user_selection) 

        if selection == 0:
            print(f"\nThanks for stopping by!")
            break
        elif selection in seats:
            seats.remove(selection)
            print("\nYour seat has been reserved!")    
        else:
            print("\nSorry. That seat is taken or doesn't exist. Please make another selection.")
    else:
        print(f"\nInvalid entry. Please enter a valid number.")

print("-" * 40)

