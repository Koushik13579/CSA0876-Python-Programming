try:
    x = input("Enter list of numbers: ")
    y = [int(num) for num in x.split()]
    avg=sum(y)/len(y)
    print("Average of list is: ",avg)
except:
    print("OOps exception occured!!!")