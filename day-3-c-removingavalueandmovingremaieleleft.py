nums = [4, 2, 5, 4]
val = 4
count = nums.count(val)
nums[:] = [num for num in nums if num != val]
k = len(nums)
nums += ['_'] * count
print("Output:", k, ", nums=", nums)
