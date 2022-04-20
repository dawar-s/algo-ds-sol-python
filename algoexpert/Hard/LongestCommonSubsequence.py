# O(mn) time | O(mn) space where m and n are the lengths of the two strings
def longestCommonSubsequence(str1, str2):
    rows = len(str2)
    cols = len(str1)
    dp = [[[] for col in range(cols + 1)] for row in range(rows + 1)]
    for row in range(1, len(dp)):
        for col in range(1, len(dp[0])):
            if str1[col-1] == str2[row-1]:
                dp[row][col] = dp[row-1][col-1] + [str2[row-1]]
            else:
                dp[row][col] = max(dp[row][col-1], dp[row-1][col], key=len)

    return dp[-1][-1]


print(longestCommonSubsequence('aaaaaa', 'aaaaaaaaa'))
