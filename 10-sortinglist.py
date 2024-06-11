inputList=list(input("Enter the list of elements(by giving space btw them): ").split())
newList=sorted(inputList,key=len)
print(newList)