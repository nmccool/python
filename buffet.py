"""
-----------------------------------------------------------------------
ASSIGNMENT: 3B - The Buffet Calculator
DATE: 2026-02-02
FILE: buffet.py
-----------------------------------------------------------------------
REQUIREMENTS:
1. Ask user for their age (convert to int).
2. Use if/elif/else to determine price:
   - Under 1: FREE ($0.00)
   - 1 to 11: $1.00 per year of age (Example: 5 years = $5.00)
   - 12 to 64: $16.95 (Standard Adult)
   - 65 and older: $12.95 (Senior Discount)
3. Print the final price formatted as currency (e.g., $16.95).
-----------------------------------------------------------------------
"""
age = int(input("How old are you? "))

# Age Group 1 "Under 1"
price_group_1 = float(0.00)

# Age Group 2 "1 to 11"
price_group_2 = float(1.00) * age

# Age Group 3 "12 to 64"
price_group_3 = float(16.95)

# Age group 4 "65 and older"
price_group_4 = float(12.95)


# Python age verification check to determine pricing
if age < 1:
    # This block runs if age is less than 1
    print(f"Your meal is FREE! ${price_group_1:.2f}")
elif age < 12:
    # This block runs if age is between 1 and 11
    print(f"Your meal is ${price_group_2:.2f} (Child Rate)")
elif age <= 64:
    # This block runs if age is between 12 and 64
    print(f"Your meal is ${price_group_3:.2f} (Standard Adult)")
else:
    # This is a catch all for ages 65 and older
    print(f"Your meal is ${price_group_4:.2f} (Senior Discount)")