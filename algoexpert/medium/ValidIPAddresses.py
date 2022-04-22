def validIPAddresses(string):
    valipIPAddresses = []
    ipAddressParts = ['', '', '', '']
    for i in range(1, 4):
        firstPart = string[:i]
        if not isValidIP(firstPart):
            continue
        ipAddressParts[0] = firstPart
        for j in range(i + 1, i + min(len(string) - i, 4)):
            secondPart = string[i:j]
            if not isValidIP(secondPart):
                continue
            ipAddressParts[1] = secondPart
            for k in range(j + 1, j + min(len(string) - j, 4)):
                thirdPart = string[j:k]
                if not isValidIP(thirdPart):
                    continue
                ipAddressParts[2] = thirdPart
                fourthPart = string[k:]
                if not isValidIP(fourthPart):
                    continue
                ipAddressParts[3] = fourthPart
                valipIPAddresses.append('.'.join(ipAddressParts))

    return valipIPAddresses


def isValidIP(text):
    if (text[0] == '0' and len(text) > 1) or int(text) > 255:
        return False
    return True
