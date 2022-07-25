def numbersInPi(pi, numbers):
    minSpaces = []
    for i in range(len(numbers)):
        current_number = numbers[i]
        if current_number[0] == '3':
            minSpaces.append(getLength(pi, numbers, current_number, 0, 0))

    minimum = float('inf')
    for num in minSpaces:
        if num < minimum and num != -1:
            minimum = num

    return minimum if minimum != float('inf') else -1


def getLength(pi, numbers, current_number, pi_idx, spaces):
    if pi_idx == len(pi):
        return spaces - 1
    if pi_idx > len(pi):
        return -1
    len_current_number = len(current_number)
    if pi[pi_idx:pi_idx + len_current_number] != current_number:
        return -1
    lst = []
    for i in range(len(numbers)):
        lst.append(getLength(pi, numbers, numbers[i], pi_idx + len_current_number, spaces + 1))
    minimum = float('inf')
    for num in lst:
        if num < minimum and num != -1:
            minimum = num

    return minimum if minimum != float('inf') else -1

print(numbersInPi('3141592653589793238462643383279',
                  ["314159265358979323846", "327", "26433", "8", "3279", "9", "314159265", "35897932384626433832", "79"]))