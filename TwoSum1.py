#!/usr/bin/python

class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        keys = {}
        for i in range(0, len(nums)):
            if target - nums[i] in keys:
                return [keys[target - nums[i]], i]
            else:
                keys[nums[i]] = i

