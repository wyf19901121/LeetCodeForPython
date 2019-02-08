class Solution:
    def removeStones(self, stones):
        """
        :type stones: List[List[int]]
        :rtype: int
        """
        #本题主要是求矩阵中有多少联通的区域，用总点数减去联通区域的个数
        #N为总点数个数
        N = len(stones)
        self.map = [-1] * 20000
        #因为坐标的数最大为10000因此，将矩阵变成一维长度为20000的向量
        for x, y in stones:
            #利用一维向量，将所有x或者y坐标相同的点合并成一个区域
            self.union(x, y + 10000)
        #最后用点的个数，减去区域的个数
        return N - len({self.find(x) for x, y in stones})

    def find(self, x):
        return x if self.map[x] == -1 else self.find(self.map[x])

    def union(self, x, y):
        fx = self.find(x)
        fy = self.find(y)
        if fx != fy:
            self.map[fx] = fy
