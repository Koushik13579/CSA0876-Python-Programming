input1=input("Enter 1st string: ")
input2=input("Enter 2nd string: ")
size=min(len(input1),len(input2))
count=0
for i in range(size):
    if input1[i]==input2[i]:
        count+=1
if count == 0:
    print("No elements match at the same index.")
else:
    print("Number of common characters in given strings is ",count)
