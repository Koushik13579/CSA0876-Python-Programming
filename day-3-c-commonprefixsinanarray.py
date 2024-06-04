def longest_common_prefix(strs):
    if not strs:
        return ""
    prefix = strs[0]
    for i in range(len(prefix)):
        for string in strs[1:]:
            if prefix[i] != string[i]:
                return prefix[:i]
    return prefix
strs1 = ["flower", "flow", "flight"]
print(longest_common_prefix(strs1))
strs2 = ["camel", "cat", "car"]
print(longest_common_prefix(strs2))
