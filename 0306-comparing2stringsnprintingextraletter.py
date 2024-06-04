sum_s = 0
sum_t = 0
s = "abcdi"
t = "abcdik"
for char in s:
    sum_s += ord(char)
for char in t:
    sum_t += ord(char)
difference = sum_t - sum_s
added_character = chr(difference)
print(added_character)
