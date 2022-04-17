def nextGreaterElement(array):
    result = [-1 for _ in range(len(array))]
    stack = []

    for i in range(2 * len(array)):
        j = i % len(array)
        while len(stack) > 0 and array[stack[-1]] < array[j]:
            top = stack.pop()
            result[top] = array[j]
        stack.append(j)
    return result
