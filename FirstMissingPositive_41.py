#  查找丢失的最小正整数


class Solution:
    def firstMissingPositive(self, nums):
        nums.sort()
        # res是最后结果，
        # 先赋值为1：1是避免nums为空就返回1；
        # 2是避免nums中所有的数都不大于0
        res = 1
        # 找到nums中第一个大于0的数
        for i in range(len(nums)):
            if nums[i] > 0:
                res = nums[i]
                break
        # 第一个大于0的数为1时，继续加1，
        # 直到新的res不在nums中时即为最小的却是正整数
        if res == 1:
            while res in nums:
                res = res + 1
        else:  # 如果最小的正整数大于1，就直接返回1
            res = 1
        return res

a = Solution()
print(a.firstMissingPositive([7, 3]))







