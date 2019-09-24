# 回文数



# # 处理小数字，将数字序列逆序，再判断是否与原来的数字相等
# def isPalindrome(x):
#
#     if x < 0:
#         return False
#     ret = 0
#     t = x
#     while t:
#         ret = ret * 10 + t % 10
#         t = t // 10
#     if ret == x:
#         return True
#     else:
#         return False
#
# print(isPalindrome(10))


# 可以将数字转化为字符串，处理大数字
def isPalindrome(x):
    if x < 0:
        return False
    s = str(x)
    s2 = s[::-1]
    if x == int(s2):
        return True
    else:
        return False

print(isPalindrome(10))

