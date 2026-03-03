"""
-----------------------------------------------------------------------
ASSIGNMENT 7B: THE MAGIC 8 BALL
-----------------------------------------------------------------------
[X] 1. Header Docstring included.
[X] 2. RESPONSES is a tuple containing at least 8 string options.
[X] 3. Program uses a 'while True' loop to keep the game running.
[X] 4. random.choice() selects the answer from the tuple.
[X] 5. Logic checks if "quit" is in the user input to break the loop.
-----------------------------------------------------------------------
Name: Neal McCool
Date: 2026-03-02
"""
import random

# 2. TODO: Create a tuple of at least 8 responses
RESPONSES = (
   "Yes",
   "No",
   "Maybe",
   "Ask again later",
   "Very Doubtful",
   "It is decidedly so",
   "Reply hazy... try again",
   "My sources say no",
   "Outlook good",
   "Without a doubt",
   "All signs point to yes"
   )

print(f"-" * 50)
print("Behold! Zoltar, The Fortune Teller!")

# 3. TODO: Create a while loop that keeps asking questions
while True:
   raw_input = input(f"Ask Zoltar a question or type 'quit' to exit: ")

# Bonus --- Sanitize ---
   clean_input = raw_input.strip().lower()

# 5. TODO: If user types "quit", break the loop --- (What if I ask "should I quit my job?" haha)
   if "quit" in clean_input:
      print(f"Zoltar thanks you. Goodbye.")
      break

# 4. TODO: Use random.choice(RESPONSES) to answer --- (Had to switch the order of 4 and 5. This wouldn't work when the 'if' was after the answer)
   answer = random.choice(RESPONSES)
   print(answer)

print(f"-" * 50)

