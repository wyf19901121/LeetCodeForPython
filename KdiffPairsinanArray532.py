class Solution:
    def findPairs(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        if k < 0:
            return 0
        count = 0
        paris = dict()
        for num in nums:
            if paris.get(num, 0) == 0:
                paris[num] = 1
            else:
                paris[num] += 1
        for key in paris.keys():
            if k == 0:
                if paris.get(key, 0) >= 2:
                    count += 1
            else:
                if paris.get(key+k, 0) != 0:
                    count += 1
        return count


