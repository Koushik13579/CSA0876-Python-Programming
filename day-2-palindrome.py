num=int(input("Enter a number: "))
temp=num
reverse=0
while temp>0:
    remainder=temp%10
    rev=(reverse*10)+remainder
    temp//=10
if(num == reverse):
    print(num,"is a palindrome.")
else:
    print(num,"is not a palindrome.")
