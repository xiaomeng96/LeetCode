# 查找元素在排序数组中的第一个和最后一个位置





# class Solution:
#     def searchRange(self, nums, target):
#
#         left = 0
#         right = len(nums)-1
#         pos = [-1, -1]
#         while left <= right:
#             if nums[left] == target:
#                 pos[0] = left
#             else:
#                 left += 1
#             if nums[right] == target:
#                 pos[1] = right
#             else:
#                 right -= 1
#             if pos[0] != -1 and pos[1] != -1:
#                 break
#         return pos


## 二分查找
# class Solution:
#     def searchRange(self, nums, target):
#         left = self.lower_bound(nums, target)
#         right = self.higher_bound(nums, target)
#         if left == right:
#             return [-1, -1]
#         return [left, right-1]
#
#     # 查找下边界，为=时，右指针向左移
#     def lower_bound(self, nums, target):
#         left = 0
#         right = len(nums)
#         while left < right:
#             mid = left + int((right - left)/2)
#             if nums[mid] < target:
#                 left = mid + 1
#             else:
#                 right = mid
#         return left
#     # 查找上边界，为=时作指针向右移
#     def higher_bound(self, nums, target):
#         left = 0
#         right = len(nums)
#         while left < right:
#             mid = left + int((right-left)/2)
#             if nums[mid] <= target:
#                 left = mid + 1
#             else:
#                 right = mid
#         return left

## python 封装的二分查找模块
import bisect
class Solution:
    def searchRange(self, nums, target):
        left = bisect.bisect_left(nums, target)
        right = bisect.bisect_right(nums, target)
        if left == right:
            return [-1, -1]
        return [left, right-1]

a = Solution()
print(a.searchRange([5,7,7,8,8,8,8,10], 8))

