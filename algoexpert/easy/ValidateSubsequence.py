def isValidSubsequence(array, sequence):
    if len(array) == 0 and len(sequence) == 0:
        return True
    if len(array) == 0:
        return False
    if len(array) < len(sequence):
        return False

    i, j = 0, 0
    while i < len(array) and j < len(sequence):
        if array[i] == sequence[j]:
            j += 1
        i += 1
        if j == len(sequence):
            return True

    return False
