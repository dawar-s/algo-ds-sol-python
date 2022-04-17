def longestPalindromicSubstring(string):
    current_longest = [0, 1]
    for i in range(1, len(string)):
        odd = getLongestPalindromeFrom(string, i - 1, i + 1)
        even = getLongestPalindromeFrom(string, i - 1, i)
        longest = max(odd, even, key=lambda x: x[1] - x[0])
        current_longest = max(longest, current_longest, key=lambda x: x[1] - x[0])
    return string[current_longest[0]: current_longest[1]]


def getLongestPalindromeFrom(string, leftidx, rightidx):
    while leftidx >= 0 and rightidx < len(string):
        if string[leftidx] != string[rightidx]:
            break
        leftidx -= 1
        rightidx += 1
    return [leftidx + 1, rightidx]
