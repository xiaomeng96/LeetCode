## 去除元素



"""
# 考察知识点
1、空间复杂度为O(1)，不能新建列表
2、remove()、遍历方法
"""
# 方法1
# class Solution:
#     def removeElement(self, nums, val):
#         while val in nums:
#             nums.remove(val)  # remove()去除第一次遇到的值
#         return len(nums)



# 方法2：使用两个指针，将指定的值都放到列表尾部
class Solution:
    def removeElement(self, nums, val):
        j = len(nums) - 1
        # 倒序遍历，步长为-1
        for i in range(len(nums) - 1, -1, -1):
            if nums[i] == val:
                nums[i], nums[j] = nums[j], nums[i]
                j -= 1
        return j+1


a = Solution()
print(a.removeElement([0, 1, 2, 2, 3, 0, 4, 2], 2))