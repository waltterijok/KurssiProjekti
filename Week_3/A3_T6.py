# Create menu program with submenus. Mainly for unit conversions. Use the values from the following table for unit conversions https://www.isa.org/getmedia/192f7bda-c77c-480a-8925-1a39787ed098/CCST-Conversions-document.pdf

# Menu options:

# Length
# Meters to kilometers
# Kilometers to meters
# Weight
# Grams to pounds
# Pounds to grams
# Exit
# “Exiting...”
# Handle all the data in floating point datatype. Remember to round every value in 1 digit precision right before displaying.

# Other possible prints:

# “Unknown option.”

print("Program starting.")
print("Welcome to the unit converter program!\nFollow the menu instructions below.")
print("Options:\n1 - Length\n2 - Weight\n0 - Exit")
choice1 = int(input("Your choice: "))
if choice1 == 1:
    print("Length options:\n1 - Meters to kilometers\n2 - Kilometers to meters\n0 - Exit")
    choice2 = int(input("Your choice: "))
    if choice2 == 1:
        meters = float(input("Insert meters: "))
        kilometers = meters / 1000
        print(f"{meters:.1f} m is {kilometers:.1f} km")
    elif choice2 == 2:
        kilometers = float(input("Insert kilometers: "))
        meters = kilometers * 1000
        print(f"{kilometers:.1f} km is {meters:.1f} m")
    elif choice2 == 0:
        print("Exiting...")
    else:
        print("Unknown option.")
elif choice1 == 2:
    print("Weight options:\n1 - Grams to pounds\n2 - Pounds to grams\n0 - Exit")
    choice2 = int(input("Your choice: "))
    if choice2 == 1:
        grams = float(input("Insert grams: "))
        pounds = grams / 453.59237
        print(f"{grams:.1f} g is {pounds:.4f} lb")
    elif choice2 == 2:
        pounds = float(input("Insert pounds: "))
        grams = pounds * 453.59237
        print(f"{pounds:.1f} lb is {grams:.1f} g")
    elif choice2 == 0:
        print("Exiting...")
    else:
        print("Unknown option.")
elif choice1 == 0:
    print("Exiting...")
else:
    print("Unknown option.")
print("\nProgram ending.")
