"""
-----------------------------------------------------------------------
ASSIGNMENT 7A: STRING MASTERY LAB
-----------------------------------------------------------------------
[X] 1. Header Docstring included with your name.
[X] 2. Task 1: String Basics (Length, Indexing, ASCII) completed.
[X] 3. Task 2: The Cleanup Crew (Strip, Case, Replace) completed.
[X] 4. Task 3: Validation (isdigit check) completed.
[X] 5. Task 4: The Duck Loop (.join and direct iteration) completed.
-----------------------------------------------------------------------
Name: Neal McCool
-----------------------------------------------------------------------
"""

# --- TASK 1: TUNING THE GUITAR 🎸 ---
instrument = "Acoustic Guitar"
# TODO: Print the length of 'instrument'
# TODO: Print the first and last letter of 'instrument'
# TODO: Use min() and max() to find and print the lowest and highest ASCII characters
print("-" * 50,"\n")
print(f"----- Instrument -----")
print(f"Variable: '{instrument}'")
# --- Length ---
print(f"Length of instrument: ", len(instrument))
# --- First and Last letter ---
print(f"First letter of instrument: ", instrument[0])
print(f"Last letter of instrument: ", instrument[-1])
# --- Highest and lowest ASCII characters ---
print(f"Lowest ASCII character: {min(instrument)}","(This is blank because the lowest character is a space)")
print(f"Highest ASCII character: {max(instrument)}")
print("\n")


# --- TASK 2: THE CLEANUP CREW 🧵 ---
messy_input = "   vOLUME_knob_11   "
# TODO: Use .strip() to remove spaces
# TODO: Use .upper() to capitalize everything
# TODO: Use .replace() to swap the underscores "_" for spaces " "
print("-" * 50,"\n")
print(f"----- Messy Input -----")
print(f"Variable: '{messy_input}'")
# --- Requested changes ---
messy_input = messy_input.strip()
print(f"Remove Spaces: '{messy_input}'")
messy_input = messy_input.upper()
print(f"Capitalize Everything: '{messy_input}'")
messy_input = messy_input.replace("_", " ")
print(f"Replace Underscores with Spaces: '{messy_input}'",("(Love the Spinal Tap reference)")) 
print("\n")

# --- TASK 3: THE VALIDATOR 🔍 ---
serial_number = "90210"
# TODO: Use .isdigit() to check validity.
# Print "Valid Serial" if it is numeric, or "Invalid Serial" if it isn't.
print("-" * 50,"\n")
print(f"----- Serial Number -----")
print(f"Serial: {serial_number}")
# --- Validation Check ---
if serial_number.isdigit():
    print(f"Valid Serial Number!")
else:
    print(f"Invalid Serial Number! Please try again.")

# --- TASK 4: THE DUCK BRIDGE 🦆🎵 ---
# We are going to sing about a Duck!
# We can't change strings (immutable), so we convert to a list
name_string = "DUCKY"
duck_letters = list(name_string)
count = 0
print("-" * 50,"\n")
print("\n--- Singing the Duck Song! ---")

# TODO: Create a loop that iterates through name_string (for char in name_string)
# TODO: Inside the loop:
#       1. Use " ".join(duck_letters) to create a variable named 'current_name'
#       2. Print: "There was a teacher who had a duck and Ducky was his Name-o"
#       3. Print the line f"({current_name}) \n" multiplied by 3
#       4. Print "and Ducky was his Name-o!\n"
#       5. Replace the letter in duck_letters at index [count] with "🦆"
#       6. Increment count by 1

for char in name_string:
# 1. --- Join ---
    current_name = " ".join(duck_letters)
# 2. --- Print ---
    print(f"There was a teacher who had a duck and Ducky was his Name-o")
# 3. --- Print * 3 ---
    print((f"({current_name})\n") * 3)
# 4. --- Print ---
    print(f"and Ducky was his Name-o!\n")
# 5. --- Replace ---
    duck_letters[count] = "🦆"
# 6. --- Count ---
    count += 1

# TODO: After the loop, print the "Finale" (the final version with all 🦆 emojis)
# Hint: You'll need one more .join() and one more print block here!

# --- Finale ---
all_ducks = "-".join(duck_letters)

print(f"There was a teacher who had a duck and Ducky was his Name-o")
print((f"({all_ducks})\n") * 3)
print(f"and Ducky was his Name-o!\n")
print("-" * 50,"\n")