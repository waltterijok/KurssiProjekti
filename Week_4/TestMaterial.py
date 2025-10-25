cornum = 23
while True:
    guess = int(input("Enter an integer: "))
    if guess == cornum:
        print("You guessed correctly!")
        print("Game ends here")
        break
    elif guess < cornum:
        print("The number is higher than your guess...")
    else:
        print("The number is lower than your guess")
print("This prints at the end, after the while loop.")

for i in range(1,8):
    print(i)
print("loop has ended")

for i in range(1,11):
    if i == 7:
      print(f"Lucky number {i} found!")
      break
    print(f"Checking number{i}")
print("Done!")