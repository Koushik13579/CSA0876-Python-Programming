s = input("Enter a string: ").lower()
s = ''.join(char for char in s if char.isalnum())
left = 0
right = len(s) - 1
while left < right:
    if s[left] != s[right]:
        print("false")
        break
    left += 1
    right -= 1
else:
    print("true")