class Solution:
    def numFriendRequests(self, ages):
        """
        :type ages: List[int]
        :rtype: int
        """
        ageRange = 121
        nums = [0] * ageRange
        sums = [0] * ageRange
        count = 0

        # 每个年龄age有多少人
        for age in ages:
            nums[age] += 1

        # 小于等于nums[i]的人数有多少
        for i in range(len(sums)):
            sums[i] += sums[i-1] + nums[i]

        for i in range(15, 121):
            if nums[i] == 0:
                continue
            j = sums[i] - sums[int(i/2)+7]
            j -= 1
            count += j * nums[i]

        return count
