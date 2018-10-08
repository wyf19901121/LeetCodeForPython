class Solution:
    def surfaceArea(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """

        area = 0
        last = 0
        for i in range(0, len(grid)):
            for j in range(0, len(grid)):
                if grid[i][j] != 0:
                    area +=1
                area += abs(grid[i][j] - last)
                last = grid[i][j]
            area += grid[i][j]
            last = 0

        for j in range(0, len(grid)):
            for i in range(0, len(grid)):
                if grid[i][j] != 0:
                    area +=1
                area += abs(grid[i][j] - last)
                last = grid[i][j]
            area += grid[i][j]
            last = 0

        return area
