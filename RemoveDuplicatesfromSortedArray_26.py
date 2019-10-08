## 从排序数组中删除重复项



"""
# 考查知识点
1、set()、遍历（去重之后顺序会改变）
2、最后要排个序
"""
class Solution:
    def removeDuplicates(self, nums):
        newlist = nums
        nums = list(set(nums))
        length = len(nums)
        nums.sort()
        for i in range(length):
            newlist[i] = nums[i]

        return length


a = Solution()
print(a.removeDuplicates([-1,0,1,1,1,2,2,3,3,4]))


