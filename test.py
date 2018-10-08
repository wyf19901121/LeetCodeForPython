#!/usr/bin/python

import sys

print(9646324351 > sys.maxsize)
print(sys.maxsize)
print(pow(2, 31) - 1)
print(9646324351 > pow(2, 31) - 1)

dp = [[0] * 5] * 3

word1 = "intention"
word2 = "execution"


len1, len2 = len(word1), len(word2)
#dp = [[0] * (len2 + 1)] * (len1 + 1)
dp = [[0] * (len2 + 1) for _ in range(len1 + 1)]

for i in range(1, len(dp)):
    for j in range(1, len(dp[0])):
        if word1[i - 1] == word2[j - 1]:
            dp[i][j] = dp[i - 1][j - 1] + 1
        else:
            dp[i][j] = max(dp[i][j - 1], dp[i - 1][j])

for i in range(0, len(dp)):
    for j in range(0, len(dp[0])):
        print("[%d][%d]=%d "%(i, j, dp[i][j]), end='')
    print('\n')

