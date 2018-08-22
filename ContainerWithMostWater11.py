class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """

        high = min(height[0], height[-1])
        maxWater = high * (len(height) - 1)

        left = 0
        right = len(height) - 1

        while left < right:
            if height[left] <= height[right]:
                left += 1
            else:
                right -= 1
            curHigh = min(height[left], height[right])
            high = max(high, curHigh)
            maxWater = max(maxWater, high * (right - left))

        return maxWater
