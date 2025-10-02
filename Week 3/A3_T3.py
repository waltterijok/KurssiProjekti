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

