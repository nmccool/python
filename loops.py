"""
-----------------------------------------------------------------------
ASSIGNMENT REQUIREMENTS
-----------------------------------------------------------------------
[X] 1. Header Docstring included.
[X] 2. Task 1: While Loop (The Nagging Kid)
       - Repeats "Are we there yet?" until user types "yes".
       - Uses a boolean variable to control the loop.
[X] 3. Task 2: For Loop (99 Bottles of Beer)
       - Counts backwards from 99 to 1.
       - Prints "[number] bottles of beer on the wall!"
[X] 4. Upload to GitHub and paste the link below.
-----------------------------------------------------------------------
"""
# Task 1: The While Loop (The Nagging Kid)
driving = True
while driving:
    print ("Are we there yet???")
    answer = input ("Are we there yet? (yes/no): ")
    # Boolean variable to stop loop
    if answer == "yes":
       driving = False
       print (f"\nYes! We made it!!! Now let's have a drink and sing a song!\n")
        
# Task 2: For Loop (99 Bottles of Beer)
for i in range(99,-1,-1):
    print (f"{i} bottles of beer on the wall, {i} bottles of beer.")
# Printed message ones loop ends
print (f"I'm drunk!")
