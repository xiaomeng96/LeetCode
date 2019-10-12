# 要求对给定顺序的数组，进行再排序，到字典排序（全排列）的下一个排序
# a1: 1,2,3;　　a2: 1,3,2;　　a3: 2,1,3;　　a4: 2,3,1;　　a5: 3,1,2;　　a6: 3,2,1;

"""
# 考察知识点
1、逆序算法编写
2、字典排序（全排列）

解决方法：
https://www.cnblogs.com/eudiwffe/p/6260699.html

"""




class Solution:
    def nextPermutation(self, nums):
        """
        Do not return anything, modify nums in-place instead.
        """
        end = len(nums) - 1
        # print(nums)
        pre = -1  ## 标记nums整个都是降序
        # 逆序遍历找到第一个相邻元素对（j，i），且A[j]<A[i]
        for i in range(end, 0, -1):  # (0, end]逆序遍历
            if nums[i-1] < nums[i]:
                j = i-1
                # print(nums[j])
                # 在(j,end]中寻找一个最小的k使其满足A[j]<A[k]。
                for k in range(end, j, -1):
                    if nums[j] < nums[k]:
                        # print(nums[k])
                        # 交换两个值的位置
                        tmp = nums[j]
                        nums[j] = nums[k]
                        nums[k] = tmp
                        break

                left = i  # 标记接下来需要翻转的起始位置
                pre = 0  # nums不是降序的
                break

        right = end
        if pre == 0:
            while left < right:
                nums[left], nums[right] = nums[right], nums[left]
                left += 1
                right -= 1
        else:
            # 找不到符合的相邻元素对，将整个nums升序
            left = 0
            while left < right:
                nums[left], nums[right] = nums[right], nums[left]
                left += 1
                right -= 1

        return nums

a = Solution()

print(a.nextPermutation([1,2,7,4,3,1]))











