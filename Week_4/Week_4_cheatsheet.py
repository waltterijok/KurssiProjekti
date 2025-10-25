children = 0
hometown = "Lahti"

# lista
TownsInFinland = ["Lahti", "Turku", "Helsinki", "Oulu", "Tampere"]  # [] lista
RandomInfo = ["Waltteri", 27, False, children, hometown]

print(TownsInFinland[0]) # printtaa listan ensimmäisen objektin
TownsInFinland.append("Rovaniemi") # .append lisää objektin listalle
print(TownsInFinland)

NumOfTowns = len(TownsInFinland) # Laskee objektien määrän listassa ja tekee siitä oman muuttujansa -> NumOfTowns
print(TownsInFinland[NumOfTowns - 1]) # printtaa listan viimeisen objektin

county = ["Asikkala", "Hollola", "Karvia", "Kempele"]
towns = ["Lahti", "Helsinki", "Lappeenranta", "Oulu", "Aulanko"]

CountiesAndTowns = [county, towns]

print(CountiesAndTowns[1][-2]) # valitsee ensin listan 1 ja sitten printattavan objektin

towns.sort()
print(towns)

teacher = {
    "name": "Juha",
    "age": 36,          # {} dictionary, oma objektinsa jossa tietoa (key)
    "city": "Lahti",
}

print(teacher["name"])

teacher["email"] = "juha.juhanen@lab.fi"    # lisää dictionaryyn objektin ja printtaa myös sen

print(teacher)

for key in teacher:
    print(key, end=" ")
    print(teacher [key])

student = [
    {"name" : "Mikko", "age" : 25, "city" : "Tampere"},
    {"name" : "Toni", "age" : 23, "city" : "Lahti"},       # dictionaryja voi myös laittaa listan sisään
    {"name" : "Anna", "age" : 26, "city" : "Helsinki"}
]
print(student)

cities = {
    "Finand" : ["Tampere", "Lahti", "Helsinki"], 
    "Sweden" : ['Stockholm', 'Malmö']               # Dictionaryssa voi olla listoja
}
print(cities["Finand"][0])

# towns = ["Lahti", "Helsinki", "Lappeenranta", "Oulu", "Aulanko"]
for town in towns:
    print(f"the town of {town}")
print(f"all of the towns {towns}")

for i in range(1,10):
    print(i)

for i in range (1,10):
    print(i, end=' ')

print()
for i in range(1, 10, 3):
    print(i)

total = 0
for i in range(1,101):
    total +=i
    print(total)

print(total)

for i in range(9):
    if i == 3:
        continue
    print(i)

# opiskele loopit for ja while sekä niihin liittyvät komennot (contiune ja break)

i = 0
while i < 10:
    print(f"Iteration number {i}")
    i += 1
    # eli i = kierros (loop) + 1

continueLoop = True
while continueLoop == True:
    if input("Do you want to continue? ") != "yes":
        continueLoop = False
    
while True:
    if input("Do you want to continue? ") != "yes":
        break
    else:
        continue