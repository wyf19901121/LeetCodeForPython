import sys


class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:

    def constructMaximumBinaryTree(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """

        if nums is None or len(nums) == 0:
            return None
        maxNum = -sys.maxsize
        maxIndex = -1
        for i in range(0, len(nums)):
            if nums[i] > maxNum:
                maxNum = nums[i]
                maxIndex = i
        root = TreeNode(maxNum)
        root.left = self.constructMaximumBinaryTree(nums[:maxIndex])
        root.right = self.constructMaximumBinaryTree(nums[maxIndex+1:])
        return root
