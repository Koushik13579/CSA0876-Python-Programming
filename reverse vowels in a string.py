s = ("leetcode")
vowels = {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'}
vowelIndices = [i for i, char in enumerate(s) if char in vowels]
reversed_vowels = [s[i] for i in reversed(vowelIndices)]
for i, index in enumerate(vowelIndices):
    s = s[:index] + reversed_vowels[i] + s[index + 1:]
print("Reversed vowels string:", s)