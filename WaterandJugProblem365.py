import math
class Solution:
    def canMeasureWater(self, x, y, z):
        """
        :type x: int
        :type y: int
        :type z: int
        :rtype: bool
        """
        if z == 0:
            return True
        if x == 0:
            return y == z
        if y == 0:
            return x == z
        return x + y >= z and z % math.gcd(x, y) == 0
