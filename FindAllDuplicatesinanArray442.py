class Solution:
    def findDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        res = set()
        for i in range(0, len(nums)):
            while nums[i] != i + 1:
                if nums[i] == nums[nums[i]-1]:
                    res.add(nums[i])
                    break
                j = nums[i]
                temp = nums[j-1]
                nums[j-1] = j
                nums[i] = temp
        return list(res)
