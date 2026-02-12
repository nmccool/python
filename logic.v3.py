"""
-----------------------------------------------------------------------
ASSIGNMENT REQUIREMENTS
-----------------------------------------------------------------------
[X] 1. Header Docstring included with your name.
[X] 2. Ask the user for their age (integer).
[X] 3. Ask the user has_id (input "yes" or "no").
[X] 4. Ask the user is_vip (input "yes" or "no").
[X] 5. Write 3 Logic Checks using if/else: 
    Gate 1 (AND): If age >= 21 and has_id == "yes", print "You may enter.", 
    Gate 2 (OR): If has_id == "yes" or is_vip == "yes", print "Welcome to the lobby." 
    Gate 3 (NOT): If not age >= 21, print "Too young!"
[X] 6. Perform 6 logical checks: (Age > 21, Age > 21, ID or VIP, Age Even, Age Not Equal 21, Not Zero).
[X] 7. Use if/elif/else to categorize Age (Positive/Negative/Zero).
[X] 8. Code is clean and uses descriptive variable names.
[X] 9. Upload to GitHub and paste the link below.

# --- 1. Assignment 4A: The Bouncer
# --- 1. Name: Neal McCool
# --- 1. Date: 2026-02-11
# --- 1. File Name: logic.v3.py
*** ---  This is an alternate assignment! --- ***
-----------------------------------------------------------------------
"""
print("\n")
print("-" * 40)
print (f"\n*** Welcome to Club SQL ***\n")

# 2. --- ASK USER FOR THEIR AGE
age = int(input(f"How old are you?: "));

# 3. --- DOES USER HAVE ID ---
if age >= 21:
    has_id = (input(f"\nDo you have some ID? (yes/no): "));

# 5a. GATE 1 (AND)
    if age >= 21 and has_id == "yes":
        print(f"\nOK, let's see it.")

# 4. --- IS USER VIP? ---
        is_vip = (input(f"\nAre you on the 'VIP List'? (yes/no): "));
    else:
        print(f"\nSorry.  Can't get in to Club SQL without ID.")        

# 5b. GATE 2 (OR)
    if age >= 21 and has_id == "yes" and is_vip == "yes":
        print(f"\nWelcome to Club SQL. You may proceed to the VIP area.");
    elif age >= 21 and has_id == "yes" or is_vip == "no":
        print(f"\nOK. You may enter Club SQL.");

# 5c. GATE 3 (NOT)
if not age >= 21:
    has_id = "no";
    is_vip = "no";
    print(f"\nGet outta here kid! You're too young and your mother is probably worried sick!")

    
# 6.  --- LOGIC STATEMENTS ---

# I THINK THIS IS WHAT YOU WERE LOOKING FOR IN THE ORIGINAL ASSIGNMENT?

print(f"\n\nLet's check those logic statements!")
print(f"\nIs the user under 21?:", not age >= 21)
print(f"Is the user over 21?", age >= 21)
print(f"Is the user's age an even number?", age % 2 == 0)
print(f"Is users age an odd number?", not age % 2 == 0)
print(f"Does user have ID or VIP?", has_id == "yes" or is_vip == "yes")
print(f"Is users age not equal to 21?", age != 21)
print(f"Is users age not zero?", age != 0 )

# 7.  --- Categorize age using if / elif / else
print(f"\nAge Categorization statements")
if age > 0:
    print("Age",age, "is positive")
elif age < 0:
    print("Age",age,"is negative")
else:
    print("Age",age, "is Zero")

print("-" * 40)


       





   