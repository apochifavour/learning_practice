def balanced_brackets(text):
    stack = []
    bracket_map = {')': '(', ']': '[', '}': '{'}
    
    for char in text:
        if char in bracket_map.values():
            stack.append(char)
        elif char in bracket_map:
            if not stack or stack[-1] != bracket_map[char]:
                return False
            stack.pop()
    return len(stack) == 0
print(balanced_brackets("((hello)"))