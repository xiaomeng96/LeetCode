# N皇后

# board = [-1 for i in range(5)]
# print(board)

# https://blog.csdn.net/weixin_38314447/article/details/79071051


class Solution:
    def solveNQueens(self, n):

        # 定义一个结果数组
        res = []
        # 初始化位置数组，用来检查某个位置是否可以放皇后
        board = [-1 for i in range(n)]

        # 定义检查函数
        def check(k, j):
            # k=depth,遍历depth之前的行
            for i in range(k):
                # (k, j) (i, board[i])
                # 检查两点的列是否相等或者两点是否在两条对角线上
                if board[i] == j or abs(k-i) == abs(j-board[i]):
                    return False
            return True

        # 定义深度遍历函数
        def dfs(depth, valuelist):
            # 递归结束条件
            if depth == n:
                res.append(valuelist)
                return
            else:
                # 遍历列
                for i in range(n):
                    # depth表示第depth+1个皇后，检查是否和前面的皇后发生冲突
                    if check(depth, i):  # 如果没有冲突
                        board[depth] = i  # 保存该位置
                        s = '.'*n
                        # 在该位置上添加皇后，继续往下一层递归
                        dfs(depth+1, valuelist+[s[:i]+'Q'+s[i+1:]])

        dfs(0, [])
        return res

a = Solution()
print(a.solveNQueens(4))


