## 将一个整数变为罗马数字


## 将数字变成数字列表并逆序，逆序遍历，i为指数级数
# 为4的时候，1和5的组合；
# 为9的时候，1和10的组合；
# 5~9之间的，5和其它数字的组合
# 1~4之间的，1的复制
# def intToRoman(num):
#
#     dict = {1: "I", 5: "V", 10: "X", 50: "L", 100: "C", 500: "D", 1000: "M"}
#     lis = list(map(int, str(num)))
#     n = len(lis)
#     # print(n)
#     lis.reverse()
#     # print(lis)
#     s = ""
#     for i in range(n-1, -1, -1):
#         if lis[i] == 4:
#             s = s + dict[pow(10, i)] + dict[5*pow(10, i)]
#         elif lis[i] == 9:
#             s = s + dict[pow(10, i)] + dict[10*pow(10, i)]
#         elif lis[i] == 5:
#             s = s + dict[5 * pow(10, i)]
#         elif lis[i] >5 and lis[i] < 9:
#             s = s + dict[5*pow(10, i)] + (lis[i]-5)*dict[pow(10, i)]
#         else:
#             s = s + lis[i]*dict[pow(10, i)]
#     return s


def intToRoman(num):
    values = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
    numerals = ["M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"]
    list = ''
    for i in range(0, len(values)):
        while num >= values[i]:
            num -= values[i]
            list += numerals[i]
    return list



print(intToRoman(1994))



