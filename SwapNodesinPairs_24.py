# 给出一条链表，交换两个相邻的节点



"""
# 考察知识点
1、链表相邻值的交换（不是单纯的交换两个节点的值）
2、建立一个头结点方便操作
"""

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def swapPairs(self, head):
        # 建立一个头结点
        newlist = ListNode(0)
        newlist.next = head

        pre = newlist
        p = pre.next

        # 至少两个节点不为空
        while p and p.next:
            tmp = p.next  # 第2个节点

            p.next = tmp.next  # 第一个节点指向第三个节点
            tmp.next = p  # 第二个节点指向第一个节点
            pre.next = tmp  # 头结点指向第二个节点


            pre = p
            p = p.next

        return newlist.next