import queue


class Solution:
    def slidingPuzzle(self, board):
        """
        :type board: List[List[int]]
        :rtype: int
        """

        goal = "123450"
        start = ""
        for i in range(0, len(board)):
            for j in range(0, len(board[0])):
                start += str(board[i][j])

        dir = [[1, 0], [0, 1], [-1, 0], [0, -1]]

        visited = set()
        visited.add(start)

        pathQueue = queue.Queue()
        pathQueue.put((start, 0))

        while not pathQueue.empty():
            curPath, curStep = pathQueue.get()
            if curPath == goal:
                return curStep
            index0 = curPath.index("0")
            path = list(curPath)
            x, y = int(index0/3), index0%3
            for pair in dir:
                tx = x + pair[0]
                ty = y + pair[1]
                if tx < 0 or tx >= 2 or ty < 0 or ty >= 3:
                    continue
                path[int(tx*3+ty)], path[int(x*3+y)] = path[int(x*3+y)], path[int(tx*3+ty)]
                pathStr = "".join(path)
                if pathStr not in visited:
                    pathQueue.put((pathStr, curStep+1))
                    visited.add(pathStr)
                path[int(tx*3+ty)], path[int(x*3+y)] = path[int(x*3+y)], path[int(tx*3+ty)]

        return -1


