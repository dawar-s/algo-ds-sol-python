def sameBsts(arrayOne, arrayTwo):
    if len(arrayOne) != len(arrayTwo):
        return False
    if isEmpty(arrayOne) and isEmpty(arrayOne):
        return True
    if arrayOne[0] != arrayTwo[0]:
        return False
    left_arrayOne, right_arrayOne = [], []
    left_arrayTwo, right_arrayTwo = [], []
    for i in range(1, len(arrayOne)):
        if arrayOne[i] < arrayOne[0]:
            left_arrayOne.append(arrayOne[i])
        else:
            right_arrayOne.append(arrayOne[i])
    for i in range(1, len(arrayTwo)):
        if arrayTwo[i] < arrayTwo[0]:
            left_arrayTwo.append(arrayTwo[i])
        else:
            right_arrayTwo.append(arrayTwo[i])

    return sameBsts(left_arrayOne, left_arrayTwo) and sameBsts(right_arrayOne, right_arrayTwo)


def isEmpty(array):
    return len(array) == 0


one = [1, 2, 3]
two = [1, 3, 2]
print(sameBsts(one, two))
one = [10, 15, 8, 12, 94, 81, 5, 2, 11]
two = [10, 8, 5, 15, 2, 12, 11, 94, 81]
print(sameBsts(one, two))
