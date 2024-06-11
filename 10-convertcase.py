word=input("Enter a string: ")
check = False
check = word.islower()
if check == True:
    print(word.upper())
else:
    print(word.lower())