"""
504. Base 7
504. 七进制数
给定一个整数，将其转化为7进制，并以字符串形式输出。

示例 1:

输入: 100
输出: "202"
示例 2:

输入: -7
输出: "-10"
注意: 输入范围是 [-1e7, 1e7]

"""

class Solution(object):
    def convertToBase7(self, num):
        """
        :type num: int
        :rtype: str
        """
        if num == 0:
            return "0"
        curNum = abs(num)
        curStr = ""
        while curNum != 0:
            curStr += str(curNum%7)
            curNum /= 7
        curStr = "".join(reversed(curStr))
        return curStr if num > 0 else "-" + curStr
