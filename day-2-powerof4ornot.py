n = int(input("Enter an integer: "))
while n > 1:
    if n % 4 != 0:
        print("false")
        break
    n /= 4
else:
    print("true")