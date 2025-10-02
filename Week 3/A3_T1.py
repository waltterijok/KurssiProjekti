print("Program starting.")
print("Insert two integers.")
first = int(input("Insert first integer: "))
second = int(input("Insert second integer: "))
print("Comparing inserted integers.")
if first == second:
    print("Integers are the same")
if first < second:
    print("Second integer is greater")
if first > second:
    print("First integer is greater")
print()
print("Adding integers together")
sum = first + second
print(f"{first} + {second} = {sum}")
print()
print("Checking the parity of the sum...")
if sum % 2 == 0:
    print("Sum is even.")
else:
    print("Sum is odd.")  
print("Program ending.")
