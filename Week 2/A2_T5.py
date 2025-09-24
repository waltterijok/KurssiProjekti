# Make a Python program, which prompts for a compound word.
# Get following aspects from the word
# Length
# First character
# Reversed version e.g. “Suitcase” is reversed “esactiuS”
# Display the aspects using print commands.
# Prompt the user to take substring from the existing compound word.
# Finally print the user specified substring.
# Example program run:

# Program starting.
print("Program starting.")

print("Program starting.")
Word = input("Insert a closed compound word: ")
print(f"The word you inserted is '{Word}' and in reverse it is '{Word[::-1]}'.")
print(f"The inserted word length is {len(Word)}")
print(f"Last character is '{Word[-1]}'")
print("Take substring from the inserted word by inserting...")
start = int((input)("1) Starting point: "))
end = int((input)("2) Ending point: "))
step = int((input)("3) Step size: "))
substring = Word[start:end:step]
print(f"The word '{Word}' sliced to the defined substring is '{substring}'.")
print("Program ending.")