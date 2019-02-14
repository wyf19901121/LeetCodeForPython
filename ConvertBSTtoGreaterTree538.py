class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def convertBST(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """

        self.getGreaterTree(root)

        return root

    def getGreaterTree(self, root, n=0):
        if root is None:
            return n
        if not root.right and not root.left:
            root.val += n
            return root.val

        rn = self.getGreaterTree(root.right, n)
        root.val += rn
        ln = self.getGreaterTree(root.left, root.val)

        return ln
