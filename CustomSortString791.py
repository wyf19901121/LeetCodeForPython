class Solution:
    def customSortString(self, S, T):
        """
        :type S: str
        :type T: str
        :rtype: str
        """

        charInS = [0] * 26
        numInT = [0] * 26

        for ch in T:
            numInT[ord(ch) - ord('a')] += 1

        res = []
        for ch in S:
            res.extend([ch] * numInT[ord(ch) - ord('a')])
            charInS[ord(ch) - ord('a')] = 1
        for i in range(0, 26):
            if charInS[i] == 0:
                res.extend(chr(97+i) * numInT[i])

        return ''.join(res)




