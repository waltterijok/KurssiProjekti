print("Program starting.\n")
startvalue = int(input("Insert starting value: "))
stopvalue = int(input("Insert stopping value: "))
start = startvalue
print("\nStarting while loop:")
while start <= stopvalue:
    print(start, end=" ")
    start += 1
print()
print("\nProgram ending.")