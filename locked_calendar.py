"""
-----------------------------------------------------------------------
ASSIGNMENT 6B: THE LOCKED CALENDAR
-----------------------------------------------------------------------
[X] 1. Header Docstring included.
[X] 2. MONTHS is defined as a constant tuple ().
[X] 3. Program uses a for loop to display each month.
[X] 4. 'try' and 'except' blocks catch a TypeError.
[X] 5. Comments explain why the modification failed.
-----------------------------------------------------------------------
Name: Neal McCool
Date: 2026-02-23
Assignment: 6B Data Integrity

"""
# 2. --- Months as tuple ---
MONTHS = ("January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December")

# 3. --- For Loop Months ---
for month in MONTHS:
    print(month)
# 4, --- Try and except to catch TypeError ---   
try:
# 5. You can't change tuples after they've been created.
    MONTHS[0] = "Smarch"
except TypeError as error:
# 5. MONTHS was created as a tuple and they are immutable.
    print("Busted! TypeError:", error)