# tee muuttuja joka laskee kierrokset
# muuta annettu arvo integeriksi
# arvo muuttuu loopin aikana
# tee while-loop joka looppaa niin kauan kun arvo ei ole 1
#     printtaa alkuperäinen arvo ja lisää loppuun ->
#     testaa onko arvo parillinen
#         jaa arvo kahdella
#     muussa tapauksessa
#         kerro arvo kolmella ja lisää 1
    
#     lisää kierroksiin +1

# printtaa kierrokset


print("Program starting.")
value = int(input("Insert a positive integer: "))
loops = 0
print(" ->", end=' ')
print(value, end='')
while value != 1:
    print(" ->", end=' ')
    if value % 2 == 0:
        value = value // 2
    else:
        value = 3 * value + 1
    print(value, end='')
    loops += 1
print()
print(f"Sequence had total {loops} steps.")
print("\nProgram ending.")
