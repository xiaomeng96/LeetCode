## 组合总和



# 解题思路：通过 sorted 函数先对候选数字的list进行排序，
# 然后再使用递归的方法来获取各个解（dfs）。
"""
# 先对candidates排序
# dfs
### target = T，从candatidates中找一个数n，新的target为T-n
    如果new_target 为0，则找到一个满足的子集；
    如果new_target < 0, 则该子集不满足，返回上一级
    如果new_target > 0, 继续往下递归
"""
class Solution:
    def combinationSum(self, candidates, target):

        sublist = []
        res = []  # 总集合
        candidates.sort()
        self.dfs(candidates, res, sublist, 0, target)
        return res

    ### 候选集合，总集合（最后所求值），当前集合，起始位置，目标值
    def dfs(self, candidates, res, sublist, start, target):
        for i in range(start, len(candidates)):
            new_target = target - candidates[i]
            if new_target < 0:
                return
            else:
                if new_target == 0:
                    res.append(sublist + [candidates[i]])
                else:
                    self.dfs(candidates, res, sublist + [candidates[i]], i, new_target)

a = Solution()
print(a.combinationSum([2,3,5], 8))

