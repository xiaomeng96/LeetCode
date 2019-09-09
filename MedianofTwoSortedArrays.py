# 两个排序数组的中位数
class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        temp = nums1 + nums2
        m = len(temp)
        temp.sort()
        if m % 2 == 1:
            median = temp[int(m/2)]
        else:
            median = (temp[int(m/2)-1] + temp[int(m/2)])/2
        return median

a = Solution()
nums1 = [1, 2]
nums2 = [3, 4]
med = a.findMedianSortedArrays(nums1, nums2)
print(med)