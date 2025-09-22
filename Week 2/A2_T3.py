# Make Python program, which prompts user to insert two words. Print the length of each word and then compound them together. Put single quotes around the compound word.
# Example program run:

# Program starting.
print("Program starting.")
# Insert first word: fire
first_word = input("Insert first word: ")
# Insert second word: fighter
second_word = input("Insert second word: ")
# 1st word is 4 characters long.
print(f"first word is {len(first_word)} characters long.")
# 2nd word is 7 characters long.
print(f"Second word is {len(second_word)} characters long.")
# Words together makes one closed compound 'firefighter'.
print(f"Words together make one closed compound '{first_word}{second_word}'")
# Program ending.
print("Program ending.")