# 三个数之和：给定一个数组A，要求从A中找出这么三个元素a,b,c使得a + b + c = 0，
# 返回由这样的a、b、c构成的三元组，且要保证三元组是唯一的。
# 参考博客：https://blog.csdn.net/m0_38109046/article/details/84866409
"""
注意问题：时间复杂度
利用中间条件排除重复的结果
"""


class Solution:
    def threeSum(self, nums):
        # 定义结果列表和子列表
        res = []
        nums.sort()  # 排序
        n = len(nums)
        for i in range(n-2):
            # 固定数nums[i]，如果和前面的数相同，就会产生相同的元组
            if i > 0 and nums[i] == nums[i-1]:
                continue
            # 定义左右指针
            left = i+1
            right = n-1
            while left < right:
                sum = nums[i] + nums[left] + nums[right]
                if sum < 0:
                    left += 1
                elif sum > 0:
                    right -= 1
                else:
                    res.append([nums[i], nums[left], nums[right]])
                    left += 1
                    right -= 1
                    # 若当前的数和上个数相同，继续寻找下一个，避免出现重复结果
                    while left < right and nums[left] == nums[left-1]:
                        left += 1
        return res


a = Solution()
print(a.threeSum([0, 0, 0, 0, 0]))


