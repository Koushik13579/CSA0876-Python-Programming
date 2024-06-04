nums = [2, 1, 2, 1, 3]
singleNum = 0
for num in nums:
    singleNum=singleNum ^ num
    print(singleNum)

print("Output:", singleNum)