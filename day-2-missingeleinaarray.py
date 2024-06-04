nums = [3, 0, 1, 5, 2]
n = len(nums)
expected_sum = n * (n + 1) // 2
actual_sum = sum(nums)
missing_number = expected_sum - actual_sum
print("Output:", missing_number)
