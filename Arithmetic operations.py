num1=float(input("Enter first number: "))
num2=float(input("Enter second number: "))
sum=num1+num2
mul=num1*num2
sub=num1-num2
print("Sum of ",num1," and ",num2," is ",sum)
print("Subtraction of ",num1," and ",num2," is ",sub)
print("multiplication of ",num1," and ",num2," is ",mul)
if(num2==0):
    print("Denominator is zero!")
else:
    print("Division of ",num1," and ",num2," is ",num1/num2)