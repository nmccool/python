"""
-----------------------------------------------------------------------
ASSIGNMENT 5A: INPUT VALIDATION
-----------------------------------------------------------------------
[X] 1. Header Docstring included.
[X] 2. All 4 inputs have 'while' loop validation.
[X] 3. The Chaperone loop uses .upper() and correct Boolean logic.
[X] 4. I have pinned a variable in the WATCH window and took a screenshot.
-----------------------------------------------------------------------
"""

# --- REGISTRATION FORM ---
print("-" * 40)

# 2.  INPUT FIELDS USING 'WHILE' LOOP VALIDATION

# --- Validate First and Last Name (Cannot be blank) ---
first_name = input("Enter First Name: ")
while first_name == "":
    print("❌ Error: First name cannot be blank.")
    first_name = input("Please Enter Your First Name: ")
last_name = input("Enter Last Name: ")
while last_name == "":
    print("❌ Error: Last name cannot be blank.")
    last_name = input("Please Enter Your Last Name: ")

# 3. Validate Chaperone Status (Must be Y or N)
chaperone = input("Parent volunteering to chaperone? (Y/N): ").upper()
while chaperone != "Y" and chaperone != "N":
    print("❌ Error: Please enter only Y or N.")
    chaperone = input("Parent volunteering to chaperone? (Y/N): ").upper()

# --- Validate Phone Number (Cannot be blank) ---
phone_number = input("Enter 10-digit phone number (e.g. 312-555-1234): ")
while len (phone_number) < 12:
        print("❌ Error: Phone number must be 10-digits in 312-555-1234 format")
        phone_number = input("Please enter 10-digit phone number: ")

print(f"\n✅ Registration Complete for {first_name} {last_name}!\n")

# --- Validate Ticket Count (Must be Integer) ---
tickets = 0
while True:
    try:
        tickets = int(input("How many tickets? "))
        if tickets > 0:
            break # Valid number! Escape the loop!
        print("❌ Error: Must be at least 1 ticket.")
    except ValueError:
        print("❌ Error: Please enter a NUMBER (e.g., 5, not 'five').")

print(f"✅ {first_name} {last_name} ordered {tickets} tickets.")
print("-" * 40)

# 4 --- Screenshot uploaded in assignment comments. ----