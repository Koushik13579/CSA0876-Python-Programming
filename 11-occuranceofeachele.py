nums=list(input("Enter list of elements: ").split())
elements={}
for num in nums:
    if num in elements:
        elements[num]+=1
    else:
        elements[num]=1
print("The number of elements in each occurance: ")
for value,count in elements.items():
    print(value,"->",count)