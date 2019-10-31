# 给定一组可能包含重复项的数字，返回所有可能的唯一排列。


class Solution:
    def permuteUnique(self, nums):
        res = []
        self.dfs(res, nums, 0)

        # new_res = []
        # # 去重
        # for s in res:
        #     if s not in new_res:
        #         new_res.append(s)
        return res

    def dfs(self, res, sublist, start):
        if start == len(sublist):
            # 注意：不能传入sublist，要传入sublist[:]（可能是深浅复制的问题）
            res.append(sublist[:])
        for i in range(start, len(sublist)):
            # start代表的是每一个子序列的第一个位置，我们每一层递归的任务都只有一个：
            # 枚举该层子序列第一个位置可以取的值
            sublist[start], sublist[i] = sublist[i], sublist[start]

            # 判断当前序列不在已有的结果中，再进入递归
            if sublist not in res:
                # 该层递归的子序列第一个位置已经确定了，所以到下一层自子序列第一个位置接着枚举
                self.dfs(res, sublist, start+1)

            # 把该层子序列的第一个位置start的值换回来，便于该层下一个枚举值的交换
            sublist[start], sublist[i] = sublist[i], sublist[start]


a = Solution()
print(a.permuteUnique([1, 1, 2, 2]))