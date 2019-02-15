import itertools

class Solution:
    def largestTimeFromDigits(self, A):
        """
        :type A: List[int]
        :rtype: str
        """
        A = sorted(A, reverse=True)
        for i in itertools.permutations(A, 4):
            hour = 10 * i[0] + i[1]
            minute = 10 * i[2] + i[3]
            if hour < 24 and minute < 60:
                return str(i[0]) + str(i[1]) + ":" + str(i[2]) + str(i[3])

        return ""
