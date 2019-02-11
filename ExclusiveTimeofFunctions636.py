class Solution:
    def exclusiveTime(self, n, logs):
        """
        :type n: int
        :type logs: List[str]
        :rtype: List[int]
        """

        res = [0] * n
        stack = []
        prev = 0
        for log in logs:
            logList = log.split(":")
            funcID, time = int(logList[0]), int(logList[-1])
            if logList[1] == 'start':
                if len(stack) != 0:
                    res[stack[-1]] += time - prev
                stack.append(funcID)
                prev = time
            if logList[1] == 'end':
                res[stack.pop()] += time - prev + 1
                prev = time + 1

        return res
