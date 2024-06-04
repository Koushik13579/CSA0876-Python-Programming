s = "({[]})"

stack = []

for char in s:
    if char == '(':
        stack.append(')')
    elif char == '[':
        stack.append(']')
    elif char == '{':
        stack.append('}')
    elif not stack or char != stack.pop():
        print("Output: false")
        break
else:
    if not stack:
        print("Output: true")
    else:
        print("Output: false")