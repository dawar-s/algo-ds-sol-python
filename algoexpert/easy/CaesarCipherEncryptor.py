def caesarCipherEncryptor(string, key):
    s = []
    key = key % 26
    for c in string:
        if (t := ord(c) + key) > 122:
            s.append(chr(t - 26))
        else:
            s.append(chr(t))

    return ''.join(s)
