class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """

        matrix = [[False] * (len(s) + 1) for i in range(len(s) + 1)]
        maxLen = 1
        left = 0
        right = 1
        matrix[len(s)][len(s)] = True
        for i in range(0, len(s)):
            matrix[i][i] = True
            matrix[i][i+1] = True
        for i in range(1, len(s)):
            for j in range(0, len(s) - i):
                matrix[j][j+i+1] = matrix[j+1][j+i] and s[j] == s[j+i]
                if matrix[j][j+i+1] and i + 1 > maxLen:
                    maxLen = i + 1
                    left = j
                    right = j + i + 1

        return s[left:right]


            

