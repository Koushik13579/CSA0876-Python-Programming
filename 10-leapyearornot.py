date=input("Enter the date: ")
year = int(date[-4:])
if (year%4 == 0 and year%100 !=0) or year%400 == 0:
    opyear=year+1
else:
    opyear=year-1
print("Input Date : ",date)
print("Output Date: ",date[:-4]+str(opyear))