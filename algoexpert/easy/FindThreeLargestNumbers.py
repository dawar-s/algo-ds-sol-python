def findThreeLargestNumbers(array):
    first, second, third = float('-inf'), float('-inf'), float('-inf')
    for num in array:
        if num > third:
            first = second
            second = third
            third = num
        elif num > second:
            first = second
            second = num
        elif num > first:
            first = num

    return [first, second, third]
