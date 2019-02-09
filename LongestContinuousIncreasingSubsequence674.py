class Solution:
    def findLengthOfLCIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        maxLen = 0
        curLen = 1
        if nums is None or len(nums) == 0:
            return maxLen
        for i in range(1, len(nums)):
            if nums[i] <= nums[i - 1]:
                maxLen = max(curLen, maxLen)
                curLen = 1
            else:
                curLen += 1
        return max(maxLen, curLen)
