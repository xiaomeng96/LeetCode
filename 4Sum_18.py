# 四数之和：解题思路和3Sum_15一样，多加一层循环

class Solution:
    def fourSum(self, nums, target):
        # 定义结果数组
        res = []
        n = len(nums)

        nums.sort()  # 排序很重要
        for i in range(n-3):  # 固定第一个数
            if i > 0 and nums[i] == nums[i-1]:  # 排除重复的元组
                continue
            # 三数之和的目标
            new_target = target - nums[i]
            # 二重循环，将四个数之和变为三个数之和的场景
            for j in range(i+1, n-2):
                if j > i+1 and nums[j] == nums[j - 1]:  # 排除重复的元组
                    continue

                left = j+1  # 忘记修改了，导致出现错误结果
                right = n-1
                while left < right:
                    sum = nums[j] + nums[left] + nums[right]
                    if sum < new_target:
                        left += 1
                    elif sum > new_target:
                        right -= 1
                    else:
                        res.append([nums[i], nums[j], nums[left], nums[right]])
                        left += 1
                        right -= 1
                        # 排除重复的元组
                        while left < right and nums[left] == nums[left-1]:
                            left += 1
        return res

a = Solution()
print(a.fourSum([-3,-1,0,2,4,5], 0))






