nums1 = [1, 2, 3]
m = 3
nums2 = [2, 5, 6]
n = 3
nums1.extend(nums2)
for i in range(m, m + n):
    j = i - 1
    key = nums1[i]
    while j >= 0 and nums1[j] > key:
        nums1[j + 1] = nums1[j]
        j -= 1
    nums1[j + 1] = key
print("Output:", nums1)
