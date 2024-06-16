arr = [10, 20, 30, 40, 50]
target = 30
index = -1
for i in range(len(arr)):
    if arr[i] == target:
        index = i
        break
if index != -1:
    print(f"Element found at index {index}")
else:
    print("Element not found")