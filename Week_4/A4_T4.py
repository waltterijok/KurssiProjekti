print("Program starting.\n")

wordcount = 0
charcount = 0

word = input("Insert word (empty stops): ")
while word != '':
    wordcount += 1
    charcount += len(word)
    word = input("Insert word (empty stops): ")

print()
print(f"You inserted:\n- {wordcount} words")
print(f"- {charcount} characters\n")

print("Program ending.")