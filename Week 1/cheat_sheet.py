print("hello world!")
print("here we are")

print("he said 'hello' 5 and kept walking")
print("he said 'hello' \n and kept walking")

exampleString = "words and numbers"
exampleInt = 12 #(kokonaisluvut)
exampleFloat = 12,2 #(numerot decimaaleilla)
exampleBoolean = False

#firstname = input("what is your first name ")
#lastname = input("what is your last name ")
#print("hello", firstname, lastname)

sentence = "finding substring"
print(sentence[0]) # palauttaa stringin ensimmäisen merkin
print(sentence[-2]) # palauttaa x merkin stringin loppupäästä
print(sentence[3:9]) # palauttaa kaiken x ja y merkin välistä
print(sentence[:9]) # palauttaa x ensimmäistä merkkiä
print(sentence[-9:-2]) # palauttaa kaiken x ja y merkkien välillä loppupäästä
print(sentence[2:9:3]) # palauttaa x, y ja z merkit
print(sentence[::3]) # palauttaa joka kolmannen merkin
print(sentence[::-1]) # palauttaa tekstin backwards
print(len(sentence)) # antaa merkkien määrän stringissä

num1 = int(input("anna luku 1 "))
num2 = int(input("anna luku 2 "))

num3 = num1 + num2
print(num3)