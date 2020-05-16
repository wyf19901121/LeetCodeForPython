"""
给定一个方阵，其中每个单元(像素)非黑即白。设计一个算法，找出 4 条边皆为黑色像素的最大子方阵。

返回一个数组 [r, c, size] ，其中 r, c 分别代表子方阵左上角的行号和列号，size 是子方阵的边长。若有多个满足条件的子方阵，返回 r 最小的，若 r 相同，返回 c 最小的子方阵。若无满足条件的子方阵，返回空数组。

示例 1:

输入:
[
   [1,0,1],
   [0,0,1],
   [0,0,1]
]
输出: [1,0,2]
解释: 输入中 0 代表黑色，1 代表白色，标粗的元素即为满足条件的最大子方阵
示例 2:

输入:
[
   [0,1,1],
   [1,0,1],
   [1,1,0]
]
输出: [0,0,1]
提示：

matrix.length == matrix[0].length <= 200
"""


class Solution:
    def findSquare(self, matrix: List[List[int]]) -> List[int]:
        maxSquare = []
        maxLen = 0
        maxRow = [[0 for i in range(len(matrix))] for j in range(len(matrix))]
        maxCol = [[0 for i in range(len(matrix))] for j in range(len(matrix))]
        for i in range(len(matrix)-1, -1, -1):
            for j in range(len(matrix)-1, -1, -1):
                if matrix[i][j] == 0:
                    maxRow[i][j] = 1 + maxRow[i][j+1] if j < len(matrix) - 1 else 1
                    maxCol[i][j] = 1 + maxCol[i+1][j] if i < len(matrix) - 1 else 1
        for i in range(len(matrix)):
            for j in range(len(matrix)):
                if len(matrix) - i <= maxLen:
                    return maxSquare
                if len(matrix) - j <= maxLen:
                    break
                minLen = min(maxRow[i][j], maxCol[i][j])
                if minLen <= maxLen:
                    continue
                for p in range(minLen, maxLen, -1):
                    if maxCol[i][j+p-1] >= p and maxRow[i+p-1][j] >= p:
                        if p > maxLen:
                            maxLen = p
                            maxSquare = [i, j, p]
        return maxSquare
