list1=list(input("Enter list of elements: ").split())
sumSqEle=sum(int(num)**2 for num in list1)
print(f"Sum of squares of elements in the list = {sumSqEle}")