# 螺旋矩阵
# https://blog.csdn.net/XX_123_1_RJ/article/details/84311952
# 要细心处理边界问题

class Solution:
    def spiralOrder(self, matrix):

        if matrix == []:
            return []

        top = 0  # 向下移动
        bottom = len(matrix) - 1  # 向上移动
        left = 0
        right = len(matrix[0]) - 1

        res = []

        while top < bottom and left < right:
            # 添加上面一行
            res += matrix[top][left:right+1]
            # 添加右边一行
            for i in range(top+1, bottom):
                res.append(matrix[i][right])
            # 添加下边一行
            res += matrix[bottom][left:right+1][::-1]
            # 添加左边一行
            for j in range(bottom-1, top, -1):
                res.append(matrix[j][left])
            # 修改四个边控制参数，将范围缩小
            top, bottom, left, right = top+1, bottom-1, left+1, right-1
        # 如果只剩下一行，最好举例确定边界条件
        if top == bottom:
            res += matrix[top][left:right+1]
        elif left == right:  # 只剩下一列
            for i in range(top, bottom+1):  # 边界条件很容易出错
                res.append(matrix[i][left])

        return res


a = Solution()
print(a.spiralOrder([
  [1, 2, 3, 4],
  [5, 6, 7, 8],
  [9,10,11,12]
]))