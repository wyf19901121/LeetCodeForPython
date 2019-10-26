"""
结果一定在S中，因此我们没有必要把S展开再求。而且这样做(当测试样例"y959q969u3hb22odq595")会出现内存溢出的现象。因此可以想办法在原始S中求第K为，1.算出展开S的长度为N，2所求位置为k%S。因此倒序遍历S，遇见数字d,N=N/d，遇见字母N=N-1;直到K%N==0。输出此处字符
"""

class Solution:
    def decodeAtIndex(self, S, K):
        """
        :type S: str
        :type K: int
        :rtype: str
        """

        length = 0
        for ch in S:
            if ch.isdigit():
                length *= int(ch)
            else:
                length += 1

        for ch in reversed(S):
            K %= length
            if K == 0 and ch.isalpha():
                return ch
            if ch.isdigit():
                length /= int(ch)
            else:
                length -= 1




