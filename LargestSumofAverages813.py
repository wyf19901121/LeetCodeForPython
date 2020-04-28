"""
我们将给定的数组 A 分成 K 个相邻的非空子数组 ，我们的分数由每个子数组内的平均值的总和构成。计算我们所能得到的最大分数是多少。

注意我们必须使用 A 数组中的每一个数进行分组，并且分数不一定需要是整数。

示例:
输入:
A = [9,1,2,3,9]
K = 3
输出: 20
解释:
A 的最优分组是[9], [1, 2, 3], [9]. 得到的分数是 9 + (1 + 2 + 3) / 3 + 9 = 20.
我们也可以把 A 分成[9, 1], [2], [3, 9].
这样的分组得到的分数为 5 + 2 + 6 = 13, 但不是最大值.
说明:

1 <= A.length <= 100.
1 <= A[i] <= 10000.
1 <= K <= A.length.
答案误差在 10^-6 内被视为是正确的。
"""

class Solution:
    def largestSumOfAverages(self, A: List[int], K: int) -> float:
        sumList = [0]
        for num in A:
            sumList.append(sumList[-1] + num)
        def average(i, j):
            return (sumList[j] - sumList[i]) / float(j - i)

        length = len(A)
        dp = [average(i, length) for i in range(length)]
        for k in range(K - 1):
            #当k为0时，即K=1，不分组，dp[i]即为下标i之后的所有数的平均值
            # 依次类推，利用动态规划公式
            for i in range(length):
                for j in range(i + 1, length):
                    dp[i] = max(dp[i], dp[j] + average(i, j))

        return dp[0]



