nums = [3, 2, 1]
disNums = set(nums)
sortedDisNums = sorted(disNums, reverse=True)
if len(sortedDisNums) >= 3:
    print(sortedDisNums[2])
else:
    print(sortedDisNums[0])