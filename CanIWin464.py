"""
464. Can I Win
464. 我能赢吗
在 "100 game" 这个游戏中，两名玩家轮流选择从 1 到 10 的任意整数，累计整数和，先使得累计整数和达到 100 的玩家，即为胜者。

如果我们将游戏规则改为 “玩家不能重复使用整数” 呢？

例如，两个玩家可以轮流从公共整数池中抽取从 1 到 15 的整数（不放回），直到累计整数和 >= 100。

给定一个整数 maxChoosableInteger （整数池中可选择的最大数）和另一个整数 desiredTotal（累计和），判断先出手的玩家是否能稳赢（假设两位玩家游戏时都表现最佳）？

你可以假设 maxChoosableInteger 不会大于 20， desiredTotal 不会大于 300。

示例：

输入：
maxChoosableInteger = 10
desiredTotal = 11

输出：
false

解释：
无论第一个玩家选择哪个整数，他都会失败。
第一个玩家可以选择从 1 到 10 的整数。
如果第一个玩家选择 1，那么第二个玩家只能选择从 2 到 10 的整数。
第二个玩家可以通过选择整数 10（那么累积和为 11 >= desiredTotal），从而取得胜利.
同样地，第一个玩家选择任意其他整数，第二个玩家都会赢。
"""

class Solution(object):


    def canIWin(self, maxChoosableInteger, desiredTotal):
        """
        :type maxChoosableInteger: int
        :type desiredTotal: int
        :rtype: bool
        """

        dp = dict()
        def search(status, total):
            """
            search函数
            status为整型，利用2进制位运算保存是否已被选，被选置位为1，否则为0
            total为整型，表示当前和
            """
            for num in range(maxChoosableInteger, 0, -1):
                if status & (1 << (num - 1)) == 0: #num还没有被选，可用
                    if total + num >= desiredTotal:
                        dp[status] = True
                        return True
                    break #最大可用的数+total都小于desiredTotal，直接结束循环

            for num in range(1, maxChoosableInteger + 1):
                if status & (1 << (num - 1)) == 0: #num还没有被选，可用
                    nextStatus = status | (1 << (num - 1))
                    if nextStatus not in dp:
                        dp[nextStatus] = search(nextStatus, total + num)
                    if dp[nextStatus] == False:
                        dp[status] = True
                        return True
            return False

        if maxChoosableInteger >= desiredTotal:
            return True
        if (1 + maxChoosableInteger) * maxChoosableInteger / 2 < desiredTotal:
            return False
        return search(0, 0)




