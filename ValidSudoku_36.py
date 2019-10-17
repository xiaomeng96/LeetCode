## 验证数独




## 方法1：采用三个矩阵检查三个规则是否有重复的数字
# class Solution:
#     def isValidSudoku(self, board):
#
#         # 初始化三个矩阵，不能用[[False]*9]*9来初始化，牵涉到深浅拷贝的问题
#         row = [[False for i in range(9)] for j in range(9)]
#         col = [[False for i in range(9)] for j in range(9)]
#         block = [[False for i in range(9)] for j in range(9)]
#
#         for i in range(9):
#             for j in range(9):
#                 if board[i][j] != '.':
#                     num = int(board[i][j]) - 1
#                     # 注意取整不能采用int(3*i/3 + j/3)，两处都需要取整
#                     k = int(i / 3) * 3 + int(j / 3)  # 表示第几个3*3矩阵块
#                     # 如果其中有一个为True，说明该数字重复出现
#                     if row[i][num] or col[j][num] or block[k][num]:
#                         return False
#                     # 出现的数字标记一下
#                     row[i][num] = col[j][num] = block[k][num] = True
#         return True


## 方法2：直接检查每个规则是否有重复
class Solution:
    def isValidSudoku(self, board):
        # 判断行规则
        for row in board:
            if not self.isValid(row):
                return False

        # 判断col规则,按列变成元组
        for col in zip(*board):
            if not self.isValid(col):
                return False

        # 3*3区块
        for i in (0, 3, 6):
            for j in (0, 3, 6):
                block = [board[x][y] for x in range(i, i+3) for y in range(j, j+3)]
                if not self.isValid(block):
                    return False

        return True

    def isValid(self, s):
        l = [i for i in s if i != '.']
        ## set()去重后是否和原来的长度相等
        return len(l) == len(set(l))




a = Solution()
b = [
  ["5","3",".",".","7",".",".",".","."],
  ["6",".",".","1","9","5",".",".","."],
  [".","9","8",".",".",".",".","6","."],
  ["8",".",".",".","6",".",".",".","3"],
  ["4",".",".","8",".","3",".",".","1"],
  ["7",".",".",".","2",".",".",".","6"],
  [".","6",".",".",".",".","2","8","."],
  [".",".",".","4","1","9",".",".","5"],
  [".",".",".",".","8",".",".","7","9"]
]
print(a.isValidSudoku(b))
