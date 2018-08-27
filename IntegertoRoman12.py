class Solution(object):
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        roman = ""

        if num/1000 != 0:
            for i in range(0, int(num/1000)):
                roman += "M"
            num %= 1000
        if num/900 != 0:
            roman += "CM"
            num -= 900
        if num/500 != 0:
            roman += "D"
            num -= 500
        if num/400 != 0:
            roman += "CD"
            num -= 400
        if num/100 != 0:
            for i in range(0, int(num/100)):
                roman += "C"
            num %= 100
        if num/90 != 0:
            roman += "XC"
            num -= 90
        if num/50 != 0:
            roman += "L"
            num -= 50
        if num/40 != 0:
            roman += "XL"
            num -= 40
        if num/10 != 0:
            for i in range(0, int(num/10)):
                roman += "X"
            num %= 10
        if num/9 != 0:
            roman += "IX"
            num -= 9
        if num/5 != 0:
            roman += "V"
            num -= 5
        if num/4 != 0:
            roman += "IV"
            num -= 4
        for i in range(0, num):
            roman += "I"

        return roman

