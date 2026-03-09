"""
-----------------------------------------------------------------------
ASSIGNMENT 8A: OPTION A - NATO TRANSLATOR
-----------------------------------------------------------------------
[X] 1. Header Docstring included.
[X] 2. NATO_ALPHABET constant is a dictionary (Full A-Z).
[X] 3. Program takes a word and uppercases it.
[X] 4. Program loops through letters and prints NATO words.
[X] 5. A 'try/except' block handles punctuation or numbers.
-----------------------------------------------------------------------
Name: Neal McCool
Date: 2026-03-09
"""
#  2.  --- Completed NATO Alphabet ---
NATO_ALPHABET = {
    "A": "Alpha", "B": "Bravo", "C": "Charlie", 
    "D": "Delta", "E": "Echo", "F": "Foxtrot",
    "G": "Golf", "H": "Hotel", "I": "Indigo",
    "J": "Juliett", "K": "Kilo", "L": "Lima",
    "M": "Mike", "N": "November", "O": "Oscar",
    "P": "Papa", "Q": "Quebec", "R": "Romeo",
    "S": "Sierra", "T": "Tango", "U": "Unifrom",
    "V": "Victor", "W": "Whiskey", "X": "Xray",
    "Y": "Yankee", "Z": "Zulu"}

print("-" * 50)
# --- Added strip function as precaution ---
word = input("Enter word to spell: ").strip().upper()

# TODO: Loop through each character
# TODO: try to print the NATO code, except if character is missing

for letter in word:
    try:
        print(NATO_ALPHABET[letter])
    except KeyError:
        print(f"Error! Please use letters only.")

print("-" * 50)
