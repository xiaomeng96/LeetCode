# N皇后问题二（输出结果不一样）


class Solution:
    res = 0  # 定义的全局变量 
    def totalNQueens(self, n):
        # 定义一个全局变量作为结果数组
        board = [-1 for i in range(n)]

        # 定义检查函数
        def check(k, j):
            # k=depth,j是要检查的皇后所在的位置
            for i in range(k):
                # 判断列和对角线的位置是否皇后和前面的皇后冲突
                if board[i] == j or abs(k-i) == abs(j-board[i]):
                    return False
            return True

        # 定义深度递归函数
        def dfs(depth):
            if depth == n:
                self.res += 1  # 要加self
                return
            else:
                # 遍历n列
                for i in range(n):
                    if check(depth, i):  # 如果没有冲突
                        board[depth] = i  # 保存该位置
                        dfs(depth+1)  # 继续摆放下一个皇后
        dfs(0)
        # 要加self
        return self.res

a = Solution()
print(a.totalNQueens(4))