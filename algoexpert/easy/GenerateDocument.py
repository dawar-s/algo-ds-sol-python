def generateDocument(characters, document):
    if document == '':
        return True
    if characters == '' or len(characters) < len(document):
        return False

    dic = {}

    for char in characters:
        if char in dic:
            dic[char] += 1
        else:
            dic[char] = 1

    for char in document:
        if char not in dic or dic[char] == 0:
            return False
        dic[char] -= 1

    return True

