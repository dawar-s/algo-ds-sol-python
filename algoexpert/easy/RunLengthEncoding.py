def runLengthEncoding(string):
    prev = string[0]
    s = []
    i = 0
    while i < len(string):
        recurr = 0
        match = False
        while i < len(string) and string[i] == prev and recurr < 9:
            i += 1
            recurr += 1
            match = True
        s.append(str(recurr) + prev)
        if i < len(string):
            prev = string[i]
            if not match:
                i += 1

    return ''.join(s)
