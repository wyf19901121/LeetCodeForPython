class Solution(object):
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """

        if str is None or len(str) == 0:
            return 0

        s = str.strip()
        if len(s) == 0:
            return 0

        signal = 1
        index = 0
        num = 0
        if s[0] == '+' or s[0] == '-':
            index += 1
            signal = -1 if s[0] == '-' else 1
        while index < len(s) and '0' <= s[index] <= '9':
            num = num * 10 + int(s[index]) - int('0')
            if num * signal > pow(2, 31) - 1 or num * signal < -pow(2, 31):
                return pow(2, 31) - 1 if signal == 1 else -pow(2, 31)
            index += 1

        return num * signal


