## 寻找插入位置


# 二分法查找
class Solution:
    def searchInsert(self, nums, target):
        left = 0
        right = len(nums)
        while left < right:
            mid = left + int((right - left)/2)
            if nums[mid] < target:
                left = mid + 1
            else:
                right = mid
        return left

a = Solution()
print(a.searchInsert([1, 3, 5, 6], 0))