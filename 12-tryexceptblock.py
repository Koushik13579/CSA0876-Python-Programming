try:
    age=int(input("Enter age:"))
    assert age>=0,"negative age is not allowed!"
    if(age>=18):
        print("you are eligible to vote!")
    else :
        rem=18-age
        print(f"you have to wait {rem} years to get eligibility of voting.")
except ValueError:
    print("ERROR: Please enter a valid integer value for age!")