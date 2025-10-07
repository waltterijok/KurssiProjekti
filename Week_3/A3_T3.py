# Create a program with a plain menu.

# Prompt username first
# Make program menu with following options:
# Print welcome message
# Welcome {Name}!
# Exit
# Exiting...
# Prompt user to choose option “Your choice:”
# Perform actions based on the user input
# Creating menus like this is a really handy way to make tiny text-based programs and there will be more exercises like this in the future.

# The expectation at this point is that the user is able to choose option by inserting corresponding number. No error handling is required, it will be introduced later.

print("Program starting.")
name = input("This is a program with a simple menu, where you can choose which operation the program performs.\n Before the menu, please insert your name: ")
print("Options:\n 1 - Print welcome message\n 0 - Exit")
print()
choice = int(input("Your choice: "))
if choice == 1:
    print(f"Welcome {name}!")
elif choice == 0:
    print("Exiting...")
else:
    print("Unknown option.")
print()
print("Program ending.")

