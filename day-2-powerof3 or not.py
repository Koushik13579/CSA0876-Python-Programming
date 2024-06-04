n = int(input("Enter an integer: "))
while n > 1:
    if n % 3!= 0:
        print("false")
        break
    n=n/3
else:
    print("true")