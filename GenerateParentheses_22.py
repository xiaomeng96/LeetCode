## 生成括号


"""
##考查知识点
1、回溯DFS
2、递归

# 如果左括号的个数还有剩余，则+’(‘然后递归，如果右括号有剩余且大于左括号的个数则+‘）’。
# 最后左右括号都不剩余的时候，也就是该排的都排完了，放入结果。
"""
class Solution:
    def generateParenthesis(self, n):
        res = []
        self.generate(n, n, '', res)
        return res

    def generate(self, l, r, str, res):
        if l == 0 and r == 0:
            res.append(str)
            return
        if l > 0:
            self.generate(l-1, r, str+'(', res)
        if r > l:
            self.generate(l, r-1, str+')', res)

a = Solution()
print(a.generateParenthesis(3))


