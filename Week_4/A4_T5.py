print("Program starting.\n")

startingpoint = int(input("Insert starting point: "))
stoppingpoint = int(input("Insert stopping point: "))
inspectpoint = int(input("Insert inspection point: "))
print('')

if startingpoint >= stoppingpoint:
    print("Starting point value must be less than the stopping point value.")

if startingpoint > inspectpoint or inspectpoint > stoppingpoint:
    print("Inspection value must be within the range of start and stop.")


elif startingpoint < stoppingpoint:
    print("First loop - inspection with break: ")
    for i in range(startingpoint, stoppingpoint):
        if i == inspectpoint:
            break
        else:
            print(i, end=' ')
    print('')
    print("Second loop - inspection with continue: ")
    for i in range(startingpoint, stoppingpoint):
        if i == inspectpoint:
            continue
        else:
            print(i, end=' ')
    print('')
print("\nProgram ending.")