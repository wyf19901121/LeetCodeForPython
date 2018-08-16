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

        for i in range(0, numRows):
            for j in range(i, len(s), 2*numRows-2):
                zs += s[j]
                if j+2*numRows-2-2*i < len(s) and i % (numRows - 1) != 0:
                    zs += s[j+2*numRows-2-2*i]

        return zs