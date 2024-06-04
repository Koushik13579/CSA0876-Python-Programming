nums = [2, 7, 11, 15]
target = 17
numIndices = {}
for i, num in enumerate(nums):
    complement = target - num
    if complement in numIndices:
        print([numIndices[complement], i])
        break
    numIndices[num] = i 