s = "cbbcd"
longest = ""
for i in range(len(s)):
    l, r = i, i
    while l >= 0 and r < len(s) and s[l] == s[r]:
        l -= 1
        r += 1
    longest = max(longest, s[l + 1:r], key=len)
    l, r = i, i + 1
    while l >= 0 and r < len(s) and s[l] == s[r]:
        l -= 1
        r += 1
    longest = max(longest, s[l + 1:r], key=len)
print(longest)