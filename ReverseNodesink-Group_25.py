# 给定一个链表，一次反转链表的k个节点并返回其修改后的列表


"""
#考察知识点
1、链表的翻转逆序
2、学习分为多步解决（多个函数）
"""



class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def reverseKGroup(self, head, k):
        if head == None or k == 1:
            return head
        # 新建一个头结点，避免头结点发生改变
        dummy = ListNode(0)
        dummy.next = head
        # 指向要翻转链表的前面位置
        pre = dummy
        cur = head
        i = 0
        while cur:
            i = i+1
            # cur走到第k个节点，获取要翻转链表的尾部，进行翻转
            if i % k == 0:
                pre = self.reverseOneGroup(pre, cur.next)
                cur = pre.next
            # 否则继续向前走
            else:
                cur = cur.next
        return dummy.next


    # 翻转函数
    def reverseOneGroup(self, pre, end):
        p = pre.next  ## 第一个节点
        cur = p.next
        # 每次交换实际上是从第二个节点开始，将每个节点放到头结点的后面
        while cur != end:
            p.next = cur.next  # 第一个节点指向第三个节点
            cur.next = pre.next  # 第二个节点指向第一个节点，放到头结点后面
            pre.next = cur  # 头结点指向第二个节点
            cur = p.next  # cur移到下个节点，准备进行下一次交换
        return p












