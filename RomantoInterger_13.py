## 将罗马数字变为整数


# # 罗马数字一般情况：从左到右，对应数字从大到小排列，特殊：IV-4（V-I)
# # 直接遍历，对于特殊的数字前后进行比较大小
# def romanToInt(s):
#
#     dict = {"I": 1, "V": 5, "X": 10, "L": 50,
#             "C": 100, "D": 500, "M": 1000}
#     n = len(s)
#     i = -1
#     sum = 0
#     while i != n-1:
#         i = i+1
#         if i == n - 1:
#             sum = sum + dict[s[i]]
#             return sum
#         if dict[s[i]] >= dict[s[i+1]]:
#             sum += dict[s[i]]
#         else:
#             sum += dict[s[i+1]] - dict[s[i]]
#             i += 1
#     return sum


def romanToInt(s):
        #从前往后扫描，用一个临时变量记录分段数字。
        #如果当前比前一个大，说明这一段的值应该是当前这个值减去上一个值。比如IV = 5 – 1；
        #否则，将当前值加入到结果中，然后开始下一段记录。比如VI = 5 + 1, II=1+1
        # 时间复杂度O(n)，空间复杂度O(1)
    dict = {'M': 1000, 'D': 500, 'C': 100, 'L': 50, 'X': 10, 'V': 5, 'I': 1}
    res = 0
    for i in range(len(s)):
        if i > 0 and dict[s[i]] > dict[s[i - 1]]:
            res += dict[s[i]] - 2*dict[s[i - 1]]
        else:
            res += dict[s[i]]
    return res







print(romanToInt("MCMXCIV"))


