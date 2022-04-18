def groupAnagrams(words):
    dic = {}
    for word in words:
        key = getkey(word)
        if key in dic:
            dic[key].append(word)
        else:
            dic[key] = [word]

    return list(dic.values())


def getkey(word):
    vocab = [0 for i in range(26)]
    key = []
    for i in range(len(word)):
        vocab[ord(word[i]) - 97] += 1
    for i in range(26):
        if vocab[i] == 0:
            continue
        key.append(str(chr(i + 97)) + str(vocab[i]))
    return ''.join(key)


words = ["yo", "act", "flop", "tac", "foo", "cat", "oy", "olfp"]
print(groupAnagrams(words))
