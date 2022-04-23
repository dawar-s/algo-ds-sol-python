def minimumCharactersForWords(words):
    maximum_frequencies = {}
    for word in words:
        word_frequency = {}
        for i in range(len(word)):
            word_frequency[word[i]] = word_frequency.get(word[i]) + 1 if word[i] in word_frequency else 1
        maximum_frequencies = {k: max(word_frequency.get(k, 0), maximum_frequencies.get(k, 0))
                               for k in set(word_frequency) | set(maximum_frequencies)}

    print(maximum_frequencies)
    lst = []
    for key, value in maximum_frequencies.items():
        for i in range(value):
            lst.append(key)

    return lst


print(minimumCharactersForWords(["this", "that", "did", "deed", "them!", "a"]))