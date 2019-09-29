## 电话号码的字母组合


"""
考察知识点：
1、递归算法
"""
# class Solution:
#     def letterCombinations(self, digits):
#         dict = ['', '1', "abc", "def", "ghi", "jkl", "mno", "pqrs", "tuv", "wxyz"]
#         if digits == "":
#             return []
#         res = ['']
#
#         def letterComb(digit, oldList):
#             return [str + i for i in dict[digit] for str in oldList]
#         # 遍历数字
#         for d in digits:
#             res = letterComb(int(d), res)
#         return res


class Solution:
    def letterCombinations(self, digits):
        # 注意dict前的self（声明为类变量）
        self.dict = {"2": 'abc', "3": 'def',
                "4": 'ghi', "5": 'jkl',
                "6": 'mno', "7": 'pqrs',
                "8": 'tuv', "9": 'wxyz'}
        if digits == '':
            return []
        res = ['']
        # print(digits[:-1])
        # print(digits[-1])
        for i in digits:
            res = self.letterComb(i, res)
        return res

    def letterComb(self, digit, oldList):
        # oldList字符串列表每项 添加 新数字对应的每个字母
        return [str+i for i in self.dict[digit] for str in oldList]


a = Solution()
print(a.letterCombinations("23"))