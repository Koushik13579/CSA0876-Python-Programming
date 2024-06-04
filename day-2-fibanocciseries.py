n=int(input("Enter number of values in series: "))
num1=0
num2=1
nextNumber=num1+num2
count=0
while count < n:
    print(num1,end=" ")
    count+=1
    num1,num2 = num2,nextNumber
    nextNumber = num1+num2