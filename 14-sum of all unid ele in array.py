def sum_of_unique_elements(nums):
    sum=0
    for num in nums:
        if nums.count(num)==1:
            sum=sum+num
    return sum

nums = input("Enter a list of elements:").split()
nums1 = [int(num) for num in nums]
print("Sum of unique elements:", sum_of_unique_elements(nums1))