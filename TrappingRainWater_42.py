## 截留雨水


# 和11题有相似之处
## 方法一：单独考虑每个位置的容量是多少
# https://blog.csdn.net/XX_123_1_RJ/article/details/81048041
class Solution:
    def trap(self, height):
        if not height:
            return 0
        res = 0
        n = len(height)
        left_max, right_max = [0]*n, [0]*n

        left_max[0] = height[0]
        for i in range(1, n):  # 从左向右扫描，求出每个位置左边最高的边
            left_max[i] = max(height[i], left_max[i-1])


        right_max[n-1] = height[n-1]
        for i in range(n-2, -1, -1):  # 从右向左扫描，求出每个位置右边最高的边
            right_max[i] = max(height[i], right_max[i+1])

        # 重新扫描每个位置，取当前位置左右最高边的短边，减去当前位置的高度值，就是当前位置的容量
        for j in range(n):
            res += min(left_max[j], right_max[j]) - height[j]

        return res


# 方法二：使用双指针法
a = Solution()
print(a.trap([0,1,0,2,1,0,1,3,2,1,2,1]))
        

