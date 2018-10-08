import math
class Solution:
    def findNthDigit(self, n):
        """
        :type n: int
        :rtype: int
        """
        nine, digit = 9, 1
        while(True):
            if n <= nine * digit:
                break
            else:
                n -= nine*digit
            nine *= 10
            digit += 1

        num = int((n-1) // digit + math.pow(10, digit-1))

        return int(str(num)[abs((n - 1) % digit)])

