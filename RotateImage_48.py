# 旋转图象（不能分配额外的空间）

# 先将矩阵上下部分交换，然后再沿着对角线交换
class Solution:
    def rotate(self, matrix):
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        # 先上下翻转
        for i in range(int(len(matrix)/2)):
            for j in range(len(matrix)):
                matrix[i][j], matrix[n-1-i][j] = matrix[n-1-i][j], matrix[i][j]

        # 再沿对角线交换（转置）
        for i in range(len(matrix)):
            for j in range(i, len(matrix)):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

        print(matrix)

a = Solution()
print(a.rotate(matrix=[[1, 2, 3],
                       [4, 5, 6],
                       [7, 8, 9]]))


# import numpy as np
# a = np.array(([1, 2, 3], [4, 5, 6], [7, 8, 9]))


# # 翻转180度
# def flip180(arr):
#     # 将arr变为大小为n*n的列表
#     new_arr = arr.reshape(arr.size)
#     # 逆序
#     new_arr = new_arr[::-1]
#     # 将列表变为(n, n)二维数组
#     new_arr = new_arr.reshape(arr.shape)
#     return new_arr
#
# # 向左旋转90度
# def flip90_left(arr):
#     new_arr = np.transpose(arr)
#     new_arr = new_arr[::-1]
#     return new_arr


# # 向右翻转90度(先向右翻转180度，再向左翻转90度)
# def flip90_right(arr):
#     new_arr = arr.reshape(arr.size)
#     new_arr = new_arr[::-1]
#     new_arr = new_arr.reshape(arr.shape)
#
#     new_arr = np.transpose(new_arr)[::-1]
#     return new_arr
#
# print(flip90_right(a))