class Solution:
    def dailyTemperatures(self, T):
        """
        :type T: List[int]
        :rtype: List[int]
        """

        indexStack = []
        res = [0] * len(T)
        for i in range(0, len(T)):
            while indexStack and T[indexStack[-1]] < T[i]:
                curIndex = indexStack.pop()
                res[curIndex] = i - curIndex
            indexStack.append(i)

        return res