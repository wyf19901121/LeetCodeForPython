class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """

        if numRows == 1 or numRows == 0 or len(s) == 0 or len(s) == 1:
            return s

        zs = ""
        for i in range(0, len(s), 2*numRows-2):
            zs += s[i]
        for i in range(1, numRows-1):
            for j in range(i, len(s), 2*numRows-2):
                zs += s[j]
                if j+2*numRows-2-2*i < len(s):
                    zs += s[j+2*numRows-2-2*i]

        for i in range(numRows-1, len(s), 2*numRows-2):
            zs += s[i]

        return zs