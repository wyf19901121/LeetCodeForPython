class Solution(object):
    def isAdditiveNumber(self, num):
        """
        :type num: str
        :rtype: bool
        """

        if len(num) < 3:
            return False

        for i in range(0, int(len(num)/2)):
            for j in range(1, len(num)):
                if len(num) - (i+j+1) < max(i+1, j):
                    break
                num1 = num[0:i+1]
                num2 = num[i+1:i+1+j]
                if len(num1) > 1 and num1[0] == '0':
                    return False
                if len(num2) > 1 and num2[0] == '0':
                    break
                if self.isAdditive(int(num1), int(num2), num[i+1+j:]) == True:
                    return True
        return False

    def isAdditive(self, left, right, other):
        if len(other) == 0:
            return True

        sum = left + right
        length = len(str(sum))
        if length > len(other):
            return False
        com = other[0:length]
        if len(com) > 1 and com[0] == '0':
            return False
        if sum != int(com):
            return False
        return self.isAdditive(right, sum, other[length:])
