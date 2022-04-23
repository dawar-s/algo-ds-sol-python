def reverseWordsInString(string: str):
    i = 0
    lst = []
    while i < len(string):
        j = string.find(' ', i)
        if j == -1:
            lst.append(string[i:])
            break
        lst.append(string[i:j])
        k = j
        while j < len(string) and string[j] == ' ':
            j += 1
        if j == len(string):
            lst.append(' ' * string.count(' ', k, len(string)))
            break
        lst.append(' ' * string.count(' ', k, j))
        i = j

    return ''.join(reversed(lst))


print(reverseWordsInString('this      string     has a     lot of   whitespace'))