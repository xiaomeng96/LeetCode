# 螺旋矩阵2
import numpy as np


class Solution:
    def generateMatrix(self, n):

        # 定义一个二维数组
        res = [[0]*n for _ in range(n)]
        # res = np.zeros((n, n), dtype=np.int)  # numpy定义

        # 定义四个边界
        rowBeg = 0
        rowEnd = n-1
        colBeg = 0
        colEnd = n-1

        tatol = n*n  # 总数量
        num = 1

        if n == 1:
            return [[1]]

        while num < tatol:
            for i in range(colBeg, colEnd+1):
                res[rowBeg][i] = num
                num += 1
            # rowBeg += 1

            for j in range(rowBeg+1, rowEnd):
                res[j][colEnd] = num
                num += 1

            for x in range(colEnd, colBeg-1, -1):
                res[rowEnd][x] = num
                num += 1

            for y in range(rowEnd-1, rowBeg, -1):
                res[y][colBeg] = num
                num += 1

            rowBeg, rowEnd, colBeg, colEnd = rowBeg+1, rowEnd-1, colBeg+1, colEnd-1

        if rowBeg == rowEnd and colBeg == colEnd:
            res[rowBeg][colBeg] = num

        return res

a = Solution()
print(a.generateMatrix(4))


