list1=list(input("Enter list of elements: ").split())
n=int(input("Enter n value(to find max and min): "))
list1=list(sorted(set(list1)))
minVal=list1[n-1]
maxValue=list1[-n]
print(f"minimum value = {minVal} and maximum value = {maxValue}")