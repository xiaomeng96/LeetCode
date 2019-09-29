## 合并两个已拍好序的链表



# 定义节点类
class ListNode:

    def __init__(self, x):
        self.val = x
        self.next = None


"""
考察的知识点：
1、链表(python类和链表的应用不太熟练)
2、链表合并（插入节点）
"""

# 两个链表都不为空的时候比较节点值大小；
# l1为空的时候，把l2直接链到合并的链表上;l2为空同理
class Solution:
    def mergeTwoLists(self, l1, l2):
        if l1 == None:
            return l2
        if l2 == None:
            return l1
        # 新建一个带有head的链表
        new_list = ListNode(0)
        tmp = new_list  # 临时链表节点
        # l1和l2都不为空的时候比较大小
        while l1 and l2:
            if l1.val <= l2.val:
                tmp.next = l1
                l1 = l1.next
            else:
                tmp.next = l2
                l2 = l2.next
            tmp = tmp.next

        if l1 == None:
            tmp.next = l2
        else:
            tmp.next = l1
        return new_list.next

a = Solution()
l1 = ListNode(1)
l2 = ListNode(1)

print(a.mergeTwoLists(l1, l2))







