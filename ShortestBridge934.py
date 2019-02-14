class Solution:
    def shortestBridge(self, A):
        """
        :type A: List[List[int]]
        :rtype: int
        """

        found = False
        dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        pointQueue = []
        count = 0

        for i in range(0, len(A)):
            for j in range(0, len(A[0])):
                if not found and A[i][j] == 1:
                    self.dfs(A, i, j)
                    found = True
                if found and A[i][j] == 1:
                    pointQueue.append((i, j))

        while pointQueue:
            size = len(pointQueue)
            for i in range(0, size):
                x, y = pointQueue.pop(0)
                for dirx, diry in dirs:
                    tx, ty = x + dirx, y + diry
                    if tx < 0 or tx >= len(A) or ty < 0 or ty >= len(A[0]):
                        continue
                    if A[tx][ty] == 0:
                        A[tx][ty] = 1
                        pointQueue.append((tx, ty))
                    if A[tx][ty] == 2:
                        return count
            count += 1

    def dfs(self, A, i, j):
        if i < 0 or i >= len(A) or j < 0 or j >= len(A[0]) or A[i][j] == 2 or A[i][j] == 0:
            return

        A[i][j] = 2
        self.dfs(A, i+1, j)
        self.dfs(A, i-1, j)
        self.dfs(A, i, j+1)
        self.dfs(A, i, j-1)
