# 在旋转排序的数组中搜索

"""
# 考察知识点
1、首尾指针的运用
# 由于时间复杂度要求为O(log n)，因此不能使用顺序遍历（其时间复杂度为O(n)）
#数组是分段有序的，前面一段从左往右递增，后面一段从右往左递减，例如[4,5,6,7,0,1,2]
#使用left、right分别从首尾同时遍历，若第一个数大于target且最后一个数小于target，返回-1
"""



class Solution:
    def search(self, nums, target):
        left = 0
        right = len(nums) - 1
        while left <= right:
            # 说明数组里面没有target
            if nums[left] > target and nums[right] < target:
                return -1
            if nums[left] == target:
                return left
            if nums[right] == target:
                return right
            # 继续向中间遍历
            left += 1
            right -= 1
        return -1

a = Solution()
print(a.search([3], 3))