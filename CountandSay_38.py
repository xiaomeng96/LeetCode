"""
# 题目解释
当n=1时：输出1；
当n=2时，解释1，1读作1个 ，表示为11；
当n=3时，解释上一个11，读作2个1，表示为21；（注意相同数字的描述）
当n=4时，解释上一个21，读作1个2，一个1，表示为1211；
当n=5时，解释上一个1211，读作1个1，1个2，2个1，表示为111221；
当n=6时，解释上一个111221，读作3个1，2个2，1个1，表示为312211；
"""

# 迭代，求出当前重复元素的个数和重复元素的值

class Solution:
    def countAndSay(self, n):
        if n <= 0:
            return ""
        res = "1"
        for i in range(1, n):
            count = 1
            tmp = ""
            for j in range(len(res)-1):
                if res[j] == res[j+1]:
                    count += 1  # 相同元素个数
                else:
                    tmp = tmp + str(count) + res[j]
                    count = 1
            # 最后一个元素
            tmp = tmp + str(count) + res[len(res)-1]
            res = tmp
        return res

a = Solution()
print(a.countAndSay(6))





