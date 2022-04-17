def phoneNumberMnemonics(phoneNumber):
    mnemonics = []
    helper(0, phoneNumber, [0] * len(phoneNumber), mnemonics)
    return mnemonics


def helper(i, phoneNumber, currentMnemonic, mnemonics):
    if i == len(phoneNumber):
        mnemonics.append(''.join(currentMnemonic))
        return
    letters = DIGITS_LETTERS[phoneNumber[i]]
    for letter in letters:
        currentMnemonic[i] = letter
        helper(i+1, phoneNumber, currentMnemonic, mnemonics)


DIGITS_LETTERS = {
    '0': ['0'],
    '1': ['1'],
    '2': ['a', 'b', 'c'],
    '3': ['d', 'e', 'f'],
    '4': ['g', 'h', 'i'],
    '5': ['j', 'k', 'l'],
    '6': ['m', 'n', 'o'],
    '7': ['p', 'q', 'r', 's'],
    '8': ['t', 'u', 'v'],
    '9': ['w', 'x', 'y', 'z']
}


print(phoneNumberMnemonics('444'))