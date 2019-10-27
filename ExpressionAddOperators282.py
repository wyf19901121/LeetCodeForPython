"""
282. Expression Add Operators
282. 给表达式添加运算符
给定一个仅包含数字 0-9 的字符串和一个目标值，在数字之间添加二元运算符（不是一元）+、- 或 * ，返回所有能够得到目标值的表达式。

示例 1:
输入: num = "123", target = 6
输出: ["1+2+3", "1*2*3"]

示例 2:
输入: num = "232", target = 8
输出: ["2*3+2", "2+3*2"]

示例 3:
输入: num = "105", target = 5
输出: ["1*0+5","10-5"]

示例 4:
输入: num = "00", target = 0
输出: ["0+0", "0-0", "0*0"]

示例 5:
输入: num = "3456237490", target = 9191
输出: []
"""

class Solution(object):
    def addOperators(self, num, target):
        """
        :type num: str
        :type target: int
        :rtype: List[str]
        """
        answerList = []
        size = len(num)

        def recurse(index, preNum, curNum, total, curList):
            if index == size:
                if total == target and curNum == 0:
                    #因初始化的原因，第一个字符为+号
                    answerList.append("".join(curList[1:]))
                return

            curNum = 10 * curNum + int(num[index])
            curStr = str(curNum)

            if curNum > 0: #第一种情况，直接扩展当前操作数，但操作数不能以0开头，增加判断
                recurse(index + 1, preNum, curNum, total, curList)

            #第二种情况，preNum和curNum之间是加号,初始化时必为+号
            curList.append('+')
            curList.append(curStr)
            recurse(index + 1, curNum, 0, total + curNum, curList)
            curList.pop()
            curList.pop()



            #因为初始阶段preNum为0，但不属于num中，所以初始阶段必须是+号，第三种情况-号，第四种情况*号，必须是curList已完成初始化
            if len(curList) > 0:
                #第三种情况-号
                curList.append('-')
                curList.append(curStr)
                recurse(index + 1, -curNum, 0, total - curNum, curList)
                curList.pop()
                curList.pop()

                #第四种情况*号
                curList.append('*')
                curList.append(curStr)
                #由于 preNum之前已经进行过加操作(减操作为+负数操作，—号情形已经进行了预处理),需要将原加减操作取消，进行乘法操作, preNum为preNum * curNum
                recurse(index + 1, preNum * curNum, 0, total - preNum + preNum * curNum, curList)
                curList.pop()
                curList.pop()

        recurse(0, 0, 0, 0, [])
        return answerList
