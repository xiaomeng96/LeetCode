import numpy
import functools

# 方法1
# map(function, iteriable,...)
# 第一个参数 function 以参数序列中的每一个元素调用 function 函数，返回包含每次 function 函数返回值的新列表。
# def reverse(self, x: int) -> int:
#     if x > 0:
#         # 将整数x转换成数字列表
#         l = list(map(int, str(x)))
#         # 再将列表中的元素倒转
#         l.reverse()
#         # 使用functools工具再变为一个整数
#         rev_data = functools.reduce(lambda x, y: x*10+y, l)
#     elif x == 0:
#         rev_data = 0
#     else:
#         x = -x
#         l = list(map(int, str(x)))
#         l.reverse()
#         rev_data = -functools.reduce(lambda x, y: x * 10 + y, l)
#     if rev_data > pow(2, 31) - 1 or rev_data < pow(-2, 31):
#         return 0
#     return rev_data


# 方法2:
# def reverse(x):
#     num = 0
#     if x == 0:
#         return 0
#     elif x < 0:
#         x = -x
#         while x != 0:
#             num = num * 10 + x % 10
#             x = x//10
#         num = -num
#     else:
#         while x != 0:
#             num = num * 10 + x % 10
#             x = x//10
#     if num > pow(2, 31) - 1 or num < pow(-2, 31):
#         return 0
#     return num

# print(reverse(120))


# 方法3：
def reverse(x):
    if x == 0:
        return 0
    symbol = ""
    if x < 0:
        symbol = "-"
        x = -x
    s = str(x)[::-1]  ## 逆转字符串
    s = symbol + s
    if int(s) > pow(2, 31)-1 or int(s) < pow(-2, 31):
        return 0
    return int(s)


print(reverse(120))




