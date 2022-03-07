# O(n) time and O(1) space - where n is length of string
def firstNonRepeatingCharacter(string):
    array = [0] * 26
    for char in string:
        array[ord(char) - 97] += 1
    for i, char in enumerate(string):
        if array[ord(char) - 97] == 1:
            return i
    return -1
