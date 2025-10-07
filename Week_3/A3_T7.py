# In this task the idea is to create a program where user can define an integer and choose the decision structure being applied to the inserted integer. Certain rules must be applied to specified value tresholds and the decision structure has partial role in the end results. Structure, order and operators matter, so do exactly as the task describes.

# Prompt user to insert value as an integer.
# Display menu
# option 1 - In one multi-branched decision
# option 2 - Independent if-statement decisions
# option 0 - Exit
# Prompt user to choose option
# Apply following math operations in the options 1 & 2
# One multi-branched decision structure:
# Value is 400 or more => add 44 to the existing value
# Value is 200 or more => add 22 to the existing value
# Value is 100 or more => add 11 to the existing value
# Independent if-statement decisions one after another:
# Value is 400 or more => add 44 to the existing value
# Value is 200 or more => add 22 to the existing value
# Value is 100 or more => add 11 to the existing value
# Exit: “Exiting…”
# At the end of the options 1 & 2, show the results like in the example program runs.
# Other possible output variats: “Unknown option.”

print("Program starting.")
print("Testing decision structures.")
num1 = int(input("Insert an integer: "))
print("Options:\n1 - In one multi branch decision\n2 - In multiple independent if statements\n0 - Exit")
choice1 = int(input("Your Choice: "))
if choice1 == 1:
    print("Using one multi branched decision structure.")
    if num1 >= 400:
        print(f"Result is {num1 + 44}")
    elif num1 >= 200:
        print(f"Result is {num1 + 22}")
    elif num1 >= 100:
        print(f"Result is {num1 + 11}")
elif choice1 == 2:
    if num1 >= 400:
        print(f"Result is {num1 + 44}")
    if num1 >= 200:
        print(f"Result is {num1 + 22}")
    if num1 >= 100:
        print(f"Result is {num1 + 11}")
elif choice1 == 0:
    print("Exiting...")
else:
    print("Unknown option.")
print("\nProgram ending.")