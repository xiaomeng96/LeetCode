#  计算x的n次幂函数


"""
解题思路：
分治+递归O(logn)
暴力求解O(n)
https://blog.csdn.net/qq_17550379/article/details/84935165
https://blog.csdn.net/XX_123_1_RJ/article/details/81143364
"""
class Solution:
    def myPow(self, x, n):

        if n == 0:  # (x的0次方为1)
            return 1.0
        if n == -1:
            return 1.0/x
        # //取整：3//-10=-4（向下），-10%3=2（余数大于大于0）
        # [1, x][n % 2]：[1, x]是一个list，[n % 2]表示下标
        return self.myPow(x*x, n//2) * ([1, x][n % 2])

a = Solution()
print(a.myPow(2.00000, -2))