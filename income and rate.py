income=int(input("Enter the value for income:"))

if(income<0):
    print("Income = ",income,"So Rate = 0.0")
elif(income<8925):
    print("Income = ",income,"So Rate = 0.10")
elif(income<36250):
    print("Income = ",income,"So Rate = 0.150")
elif (income <87850):
    print("Income = ", income, "So Rate = 0.2000")
else:
    print("Income = ", income, "So Rate = 0.2500")

