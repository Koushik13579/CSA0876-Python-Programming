arr=[1,5,2,0,8,6]
n=len(arr)
for i in range(n):
    for j in range(n-1):
        if arr[j]>arr[j+1]:
            arr[j],arr[j+1]=arr[j+1],arr[j]
print("Sorted list :",arr)
