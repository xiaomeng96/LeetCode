## 全排列

"""
#考察知识点
1、dfs
2、全排列（与31题相似）
3、交换两个数
4、https://blog.csdn.net/GetterAndSetter/article/details/81516259
"""

class Solution:
    def permute(self, nums):
        result = []
        self.dfs(result, nums, 0)
        return result

    def dfs(self, res, sublist, start):
        if start == len(sublist):
            # 注意：不能传入sublist，要传入sublist[:]（可能是深浅复制的问题）
            res.append(sublist[:])
        for i in range(start, len(sublist)):
            # start代表的是每一个子序列的第一个位置，我们每一层递归的任务都只有一个：
            # 枚举该层子序列第一个位置可以取的值
            sublist[start], sublist[i] = sublist[i], sublist[start]
            # 该层递归的子序列第一个位置已经确定了，所以到下一层第一个位置接着枚举
            self.dfs(res, sublist, start+1)
            # 把该层子序列的第一个位置start的值换回来，便于下一个枚举值的交换
            sublist[start], sublist[i] = sublist[i], sublist[start]

a = Solution()
print(a.permute([1, 2, 3]))

