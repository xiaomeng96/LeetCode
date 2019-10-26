## 不能重复使用候选集合中的数字



class Solution:
    def combinationSum(self, candidates, target):

        sublist = []
        res = []  # 总集合
        candidates.sort()
        self.dfs(candidates, res, sublist, 0, target)

        # new_res = []
        # for i in res:
        #     if i not in new_res:
        #         new_res.append(i)
        return res

    ### 候选集合，总集合（最后所求值），当前集合，起始位置，目标值
    def dfs(self, candidates, res, sublist, start, target):
        # for循环实际上是横着遍历，递归是往下延伸
        for i in range(start, len(candidates)):
            new_target = target - candidates[i]
            if new_target < 0:
                return
            else:
                if new_target == 0:
                    # 保证最后的结果res中没有重复值
                    if sublist + [candidates[i]] not in res:
                        res.append(sublist + [candidates[i]])
                else:
                    # 元素不能重复使用，递归的起始位置要从i+1开始
                    self.dfs(candidates, res, sublist + [candidates[i]], i+1, new_target)

a = Solution()
print(a.combinationSum([10, 1, 2, 7, 6, 1, 5], 8))