class Solution(object):
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
        pre1 = 1
        pre2 = self.getDecodeingsNum(s[0:1])
        for i in range(1, len(s)):
            cur = pre2 * self.getDecodeingsNum(s[i:i+1]) + \
                 pre1 * self.getDecodeingsNum(s[i-1:i+1])
            pre1 = pre2
            pre2 = cur % 1000000007
        return pre2

    def getDecodeingsNum(self, s):
        if len(s) == 1:
            if s[0] == '*':
                return 9
            return 0 if s[0] == '0' else 1
        if s == '**':
            return 15
        elif s[1] == '*':
            if s[0] == '1':
                return 9
            return 6 if s[0] == '2' else 0
        elif s[0] == '*':
            return  2 if s[1] < '7' else 1
        else:
            return 1 if 10 <= int(s) <= 26 else 0
