# 把字符排成Z字形，再按照行的顺序依次拼接到一起，形成新的字符串

"""
解题思路：
找规律（Z字形后，字符下标的规律）
https://yq.aliyun.com/articles/708328
https://blog.csdn.net/fuxuemingzhu/article/details/80830509
"""


class Solution:
    def convert(self, s, numRows):
        if numRows == 1:
            return s

        res = ""  # 定义结果字符串
        interval = 2*(numRows - 1)  # 第一行两个字符下标的间隔
        # 首行
        for i in range(0, len(s), interval):  # 间隔为interval
            res += s[i]

        # 中间行
        for row in range(1, numRows-1):
            inter = 2*row
            i = row
            while(i < len(s)):
                res += s[i]
                inter = interval - inter  # 规律：interval-2i, 2i....
                i += inter

        # 最后一行
        for i in range(numRows-1, len(s), interval):
            res += s[i]

        return res


a = Solution()
print(a.convert("PAYPALISHIRING", 4))




