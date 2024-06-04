num1=int(input("Enter first number:" ))
num2=int(input("Enter second number:" ))
num3=int(input("Enter third number:" ))

if (num1<=num2) and (num1<=num3):
    print("num1=",num1,"is the least among the input numbers.")
elif (num2<=num1) and (num2<=num3):
    print("num2=",num2,"is the least among the input numbers.")
else:
    print("num3=", num3, "is the least among the input numbers.")
