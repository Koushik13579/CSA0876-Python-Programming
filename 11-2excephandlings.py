try:
    num = int(input("Enter the value of numerator: "))
    den = int(input("Enter the value of denominator: "))
    result = num/den
    print("Result :%.2f"%result)
except ZeroDivisionError:
    print("Error : Denominator zero is not Allowed.")
except ValueError:
    print("Error: Enter a valid numeric values.")