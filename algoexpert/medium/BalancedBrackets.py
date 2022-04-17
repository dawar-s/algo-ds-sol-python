def balancedBrackets(string):
    stack = []
    for char in string:
        if char in OPENING_BRACKETS:
            stack.append(char)
        elif char in CLOSING_BRACKETS:
            if len(stack) == 0:
                return False
            if stack[-1] != MATCHING_BRACKETS[char]:
                return False
            stack.pop()

    return len(stack) == 0


OPENING_BRACKETS = ['(', '[', '{']
CLOSING_BRACKETS = [')', ']', '}']
MATCHING_BRACKETS = {')': '(', ']': '[', '}': '{'}
