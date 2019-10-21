## 编写一个程序，通过填充空单元格来解决数独难题。




# 八皇后问题，回溯法

class Solution:
    def solveSudoku(self, board):
        """
        Do not return anything, modify board in-place instead.
        """
        def isValid(x, y):
            # 判断列是否有重复
            for i in range(9):
                if i != x and board[i][y] == board[x][y]:
                    return False

            # 判断行是否有重复
            for j in range(9):
                if j != y and board[x][j] == board[x][y]:
                    return False

            # 判断3*3块中是否有重复
            for i in range(int(x/3)*3, int(x/3)*3+3):
                for j in range(int(y/3)*3, int(y/3)*3+3):
                    if i != x and j != y and board[i][j] == board[x][y]:
                        return False
            return True

        def dfs(board):
            for i in range(9):
                for j in range(9):
                    if board[i][j] == '.':
                        for c in "123456789":
                            board[i][j] = c
                            if isValid(i, j) and dfs(board):
                                return True
                            board[i][j] = '.'
                        # c值都不满足，返回False
                        return False
            # 所有的都遍历完了
            return True

        dfs(board)

print(Solution().solveSudoku([
  ["5","3",".",".","7",".",".",".","."],
  ["6",".",".","1","9","5",".",".","."],
  [".","9","8",".",".",".",".","6","."],
  ["8",".",".",".","6",".",".",".","3"],
  ["4",".",".","8",".","3",".",".","1"],
  ["7",".",".",".","2",".",".",".","6"],
  [".","6",".",".",".",".","2","8","."],
  [".",".",".","4","1","9",".",".","5"],
  [".",".",".",".","8",".",".","7","9"]
]))                         
