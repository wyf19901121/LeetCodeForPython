"""
输入一个整数数组，实现一个函数来调整该数组中数字的顺序，使得所有奇数位于数组的前半部分，所有偶数位于数组的后半部分。

示例：
输入：nums = [1,2,3,4]
输出：[1,3,2,4]
注：[3,1,2,4] 也是正确的答案之一。
 
提示：
1 <= nums.length <= 50000
1 <= nums[i] <= 10000
"""

class Solution:
    def exchange(self, nums: List[int]) -> List[int]:
        j = 0
        for i in range(len(nums)):
            if nums[j]%2 == 1:
                j += 1
            elif nums[i]%2 == 1:
                temp = nums[j]
                nums[j] = nums[i]
                nums[i] = temp
                j += 1

        return nums

