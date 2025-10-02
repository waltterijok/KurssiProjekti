print("Program starting.")
print()
print("Options:\n 1 - Celsius to Fahrenheit\n 2 - Fahrenheit to Celsius\n 0 - Exit")
choice = int(input("Your choice: "))
if choice == 1:
    celsius = float(input("Insert the amount of Celsius: "))
    fahrenheit = (celsius * 1.8) + 32
    print(f"{celsius} C equals to {fahrenheit} F")
elif choice == 2:
    fahrenheit = float(input("Insert the amount of fahrenheit: "))
    celsius = (fahrenheit - 32) / 1.8
    print(f"{fahrenheit} F equals to {round(celsius,1)} C")
elif choice == 0:
    print("Exiting...")
else:
    print("Unknown option")
print()
print("Program ending.")
    
    