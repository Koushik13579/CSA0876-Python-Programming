try:
    x = input("Enter list of numbers: ")
    y = [int(num) for num in x.split()]
    if not y:
        raise ZeroDivisionError("The list is empty.")
    avg=sum(y)/len(y)
    print("Average of list is: ",avg)
except ValueError as e:
    print(f"An error occurred: {e}")
except ZeroDivisionError as e:
    print(f"An error occured: {e}")