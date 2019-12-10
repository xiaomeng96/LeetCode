# 字符串相乘（大数乘法）


class Solution:
    def multiply(self, num1, num2):
        l1, l2 = len(num1), len(num2)
        res = ['0']*(l1+l2)  # 最好不要定义为字符串，否则后面会出现问题
        # 若为空字符串，返回空字符串
        if l1 == 0 or l2 == 0:
            return ""

        for i in range(l1-1, -1, -1):
            # 记录进位
            add = 0
            for j in range(l2-1, -1, -1):
                # 当前位数的乘积，字符化为数字计算
                mul = int(num1[i])*int(num2[j])
                # 当前位置数字 + 上一个位置的进位 + 乘积的个位数
                sum = int(res[i+j+1]) + add + mul % 10
                # 得到当前位置新的值，变为字符保存
                res[i+j+1] = str(sum % 10)
                # 计算当前位置的进位(注意除法要取整）
                add = int(mul / 10) + int(sum / 10)

            res[i] = str(add)
        for i in range(len(res)):
            if res[i] != '0':
                return ''.join(res[i:])
        # 其中一个数为0的情况
        return '0'


a = Solution()
print(a.multiply("8", "99"))











