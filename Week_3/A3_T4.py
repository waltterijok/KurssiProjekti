# Extend the previous menu program by adding three more options to the menu.

# Options:

# Print the name backwards
# Your name backwards is "{NameBackwards}"
# Print the first character
# The first character in name "{Name}" is "{FirstChar}"
# Show the amount of characters in the name
# There are {NameLength} characters in the name "{Name}"

print("Program starting.")
name = input("This is a program with a simple menu, where you can choose which operation the program performs.\n Before the menu, please insert your name: ")
print("Options:\n 1 - Print welcome message\n 2 - Print name backwards\n 3 - Print the first character\n 4 - Show the amount of characters in the name\n 0 - Exit")
print()
choice = int(input("Your choice: "))
if choice == 1:
    print(f"Welcome {name}!")
elif choice == 2:
    print(f"Your name backwards is {name[::-1]}")
elif choice == 3:
    print(f"The first character in the name '{name[0]}'")
elif choice == 4:
    print(f"there are {len(name)} characters on the name '{name}'")
elif choice == 0:
    print("Exiting...")
else:
    print("Unknown option.")
print()
print("Program ending.")