class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        index = 1 if x >=0 else -1

        lx = long(abs(x))
        lr = 0

        while lx != 0:
            lr = lr * 10 + lx % 10
            lx /= 10

        lr *= index
        if lr > pow(2, 31) - 1 or lr < -pow(2, 31):
            return 0

        return int(lr)

