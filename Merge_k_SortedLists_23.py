## 合并k条排好序的链表




"""
## 考察知识点
1、链表合并操作
2、递归（先写出合并两条链表的函数，调用k次，递归带入合并好的链表和新链表）
"""
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def mergeKLists(self, lists):
        if len(lists) == 0:
            return None
        res = lists[0]
        for i in range(1, len(lists)):
            res = self.mergeTwoLists(res, lists[i])
        return res


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






