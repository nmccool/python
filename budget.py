"""
-----------------------------------------------------------------------
ASSIGNMENT REQUIREMENTS
-----------------------------------------------------------------------
[x] 1. Header Docstring included.
[x] 2. Ask user for Monthly Income (float).
[x] 3. Ask user for 5 DIFFERENT expense amounts (float).
[x] 4. Calculate Total Expenses and Remaining Balance.
[x] 5. Calculate Percentage of Income Spent.
[x] 6. Output formatted to 2 decimal places (:,.2f or :.2%).
-----------------------------------------------------------------------
"""
# --- 1. ASSIGNMENT 3A: Number Formatting and Math
# --- 1. Date: 2026-02-02
# --- 1. File Name: budget.py

# --- "The Personal Budget" ---
 
# --- 2. GET INPUT ---
gross_pay = float(input("Enter your Monthly Income: $"))

# --- 3. GET EXPENSES ---
expense1 = float(input("Enter Rent/Mortgage amount: $"))
expense2 = float(input("Enter Cell Phone amount: $"))
expense3 = float(input("Enter Car Insurance amount: $"))
expense4 = float(input("Enter Gasoline amount: $"))
expense5 = float(input("Enter Groceries amount: $"))

# --- 4. CALCULATE TOTAL EXPENSES AND REMAINING BALANCE ---
total_expenses = expense1 + expense2 + expense3 + expense4 + expense5
remaining_balance = gross_pay - total_expenses
remaining_balance_percentage = remaining_balance / gross_pay

# --- 5. CALCULATE PERCENTAGE OF INCOME SPENT ---
percentage_spent = total_expenses / gross_pay   

# --- 6. OUTPUT RESULTS ---
print(f"\n\n")
print(f"--- Personal Budget ---")
print(f"Monthly Income = ${gross_pay:,.2f}")
print(f"Total Expenses = ${total_expenses:,.2f}")
print(f"Percentage Spent = {percentage_spent:,.2%}")
print(f"Remaining Balance = ${remaining_balance:,.2f}")
print(f"Percentage Remaining = {remaining_balance_percentage:,.2%}")