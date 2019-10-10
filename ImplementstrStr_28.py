## 实现strStr()

##问题：当 needle 是空字符串时，我们应当返回什么值呢？
# 返回0



## 方法一：find()检测字符串中是否包含子字符串 str ，如果指定beg（开始）和end（结束）范围，
# 则检查是否包含在指定范围内，如果包含子字符串返回开始的索引值，否则返回-1。
# class Solution:
#     def strStr(self, haystack, needle):
#
#         return haystack.find(needle)



## 方法二：暴力破解法
# 从字符串haystack的每个位置开始，截取和needle相同长度的字串，与needle进行比较
class Solution:
    def strStr(self, haystack, needle):
        for i in range(len(haystack)):
            if haystack[i: i+len(needle)] == needle:
                return i
        return -1




a = Solution()
print(a.strStr("aaaaa", ""))

