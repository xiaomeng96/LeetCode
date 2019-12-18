# 求一个数组的最大子段和



# 方法一：暴力求解O(n2)
# https://www.cnblogs.com/wf751620780/p/9285782.html

# class Solution:
#     def maxSubArray(self, nums):
#         if len(nums) == 0:
#             return 0
#
#         maxSum = float('-inf')
#         for i in range(len(nums)):
#             sum = 0
#             for j in range(i, len(nums)):
#                 sum += nums[j]
#                 maxSum = max(maxSum, sum)
#         return maxSum
#
# a = Solution()
# print(a.maxSubArray([-2,1,-3,4,-1,2,1,-5,4]))


# 方法二：动态规划O(n)
# https://www.jianshu.com/p/59e06902bd3a
# class Solution:
#     def maxSubArray(self, nums):
#         maxSum = float('-inf')
#         pre = 0
#         if len(nums) == 0:
#             return 0
#         for i in range(len(nums)):
#             # 前面最大子串之和
#             pre = max(pre+nums[i], nums[i])
#             maxSum = max(maxSum, pre)
#
#         return maxSum
#
# a = Solution()
# print(a.maxSubArray([-2,1,-3,4,-1,2,1,-5,4]))


# 方法三：分治算法O(nlog2n)
# https://blog.csdn.net/HaixWang/article/details/80719804
class Solution:
    def maxSubArray(self, nums):
        # 递归的结束条件，否则会出现错误
        if len(nums) == 1:
            return nums[0]
        n = len(nums)
        mid = n // 2  # 取整
        # 最大子序列在左边
        left_sum = self.maxSubArray(nums[:mid])
        # 最大子序列在右边
        right_sum = self.maxSubArray(nums[mid:])
        # 最大子序列在中间
        cross_sum = self.crossing_maxSubArray(nums[:mid], nums[mid:])
        return max(left_sum, right_sum, cross_sum)

    def crossing_maxSubArray(self, left, right):
        left_sum, right_sum = float('-inf'), float('-inf')
        sum = 0
        # 左边的最大后缀，逆序遍历
        for i in range(len(left)-1, -1, -1):
            sum += left[i]
            left_sum = max(left_sum, sum)

        # 右边的最大前缀
        sum = 0
        for i in range(len(right)):
            sum += right[i]
            right_sum = max(right_sum, sum)

        return left_sum+right_sum

a = Solution()
print(a.maxSubArray([-2,1,-3,4,-1,2,1,-5,4]))






