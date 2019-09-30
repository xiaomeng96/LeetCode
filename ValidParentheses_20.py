## 有效的括号


"""
### 考察知识点
1、栈（后进先出）



解题思路
遍历字符串的每个字符：
如果字符是左半边括号（即(,[,{),将字符压栈；
如果是右半边字符，此时，先判断栈是否为空，
    如果栈为空，则该字符无法找到匹配的括号，返回False
    如果栈不为空，则弹出栈顶元素并与之比较
        如果两个字符不匹配，则返回False
        如果匹配的话，就删除栈顶元素（此处用list模拟栈）
最后判断stack是否为空
    为空，匹配完毕，返回True
    不为空，有字符没有匹配完，返回False
"""
class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        dict = {'(': ')', '[': ']', '{': '}'}
        if len(s)%2 != 0:
            return False
        for str in s:
            # 左括号压栈
            if str == '(' or str == '[' or str == '{':
                stack.insert(0, str)
            # 右括号，先判断stack是否为空，为空的话返回False
            elif len(stack) == 0:
                return False
            # stack不为空的话，比较两个元素是否匹配，匹配就删除栈顶元素
            elif dict[stack[0]] == str:
                del stack[0]
            # 两个元素不匹配，返回False
            else:
                return False
        if len(stack) == 0:
            return True
        else:
            return False


a = Solution()
print(a.isValid("))))"))