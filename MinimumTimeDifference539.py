class Solution(object):
    def findMinDifference(self, timePoints):
        """
        :type timePoints: List[str]
        :rtype: int
        """

        def convert(time):
            return int(time[:2]) * 60 + int(time[3:])
        timePoints = map(convert, timePoints)
        timePoints.sort()
        return min((y - x) % (24 * 60) for x, y in zip(timePoints,
                timePoints[1:] + timePoints[:1]))
