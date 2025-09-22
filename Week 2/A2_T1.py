#program starting.
print("Program starting.")
# What is your name: John
feed = input("What is your name: ")
name = feed
# Enter a floating point number: 3.1
feed = input("Enter a floating point number: ")
num1 = float(feed)
# Enter second floating point number: 5.3
feed = input("Enter second floating point number: ")
num2 = float(feed)
# John you gave numbers 3.1 and 5.3
print(f"{name} gave you numbers {num1} and {num2}")
product = num1 * num2
product = round(product, 2)
# Multiplying first and second number will result in product
print(f"Multiplying first and second number will result in product {product}")
#program ending.
print("Program ending.")