import math
class Solution:
    def hasGroupsSizeX(self, deck):
        """
        :type deck: List[int]
        :rtype: bool
        """
        hcf = 0
        countMap = dict()
        for num in deck:
            if countMap.get(num, 0) == 0:
                countMap[num] = 1
            else:
                countMap[num] += 1
        for k, v in countMap.items():
            if hcf == 0:
                hcf = v
            hcf = math.gcd(hcf, v)
            if hcf == 1:
                return False

        return True