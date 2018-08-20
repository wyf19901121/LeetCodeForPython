class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """

        if x < 0:
            return False

        y = x
        div = 1
        while y >= 10:
            y /= 10
            div *= 10

        while div >= 10:
            if x / div != x % 10:
                return False
            x %= div
            x /= 10
            div /= 100

        return True
