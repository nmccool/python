"""
-----------------------------------------------------------------------
ASSIGNMENT REQUIREMENTS
-----------------------------------------------------------------------
[ ] 1. Header Docstring included with your name.
[ ] 2. Ask user for two integers (num1 and num2).
[ ] 3. Perform 6 logical checks: (Both > 0, Both > 100, Either Even, Either < 100, Not Equal, Not Zero).
[ ] 4. Use if/elif/else to categorize num1 (Positive/Negative/Zero).
[ ] 5. Code is clean and uses descriptive variable names.
[ ] 6. Upload to GitHub and paste the link below.

# --- 1. Assignment 4A: The Logic Gate
# --- 1. Name: Neal McCool
# --- 1. Date: 2026-02-09
# --- 1. File Name: logic2cheat.py
-----------------------------------------------------------------------
"""
# --- GET USER INPUT ---
num1 = int(input("Add up all of the numbers in your birthdate and enter the total here: "))
num2 = int(input("Add up all of the numbers in today's date and enter them here: "))

print("\n--- Logical Checks ---")

# 1. Both > 0
print("Both numbers are greater than 0:", num1 > 0 and num2 > 0)

# 2. Both > 100
print("Both numbers are greater than 100:", num1 > 100 and num2 > 100)

# 3. Either Even
print("At least one number is even:", num1 % 2 == 0 or num2 % 2 == 0)

# 4. Either < 100
print("At least one number is less than 100:", num1 < 100 or num2 < 100)

# 5. Not Equal
print("The numbers are not equal:", num1 != num2)

# 6. Not Zero
print("Neither number is zero:", num1 != 0 and num2 != 0)

print("\n--- num1 Categorization ---")

# Categorize num1 using if / elif / else
if num1 > 0:
    print("num1 is Positive")
elif num1 < 0:
    print("num1 is Negative")
else:
    print("num1 is Zero")