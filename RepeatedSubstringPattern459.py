class Solution:
    def repeatedSubstringPattern(self, s):
        """
        :type s: str
        :rtype: bool
        """

        firstIndexs = []
        for i in range(1, int(len(s)/2 + 1)):
            if s[i] == s[0]:
                firstIndexs.append(i)

        for i in firstIndexs:
            if s[:i] * int(len(s)/i) == s:
                return True

        return False
