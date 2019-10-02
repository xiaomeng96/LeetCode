## 从链表的末端移除第n个节点


"""
##考察知识点：
1、链表的操作
2、链表的删除
"""

## 链表末端第n个节点可以转换为链表首端的第len(list)-n+1个节点；
# 遍历链表到要删除的点
# 临时变量pre = head; p = pre.next
# 删除节点pre.next = p.next; free(p)
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def removeNthFromEnd(self, head, n):
        if n == 0:
            return head
        len = 0
        # 获取链表总长度时，要建立一个临时变量，否则原链表的指针会走到末尾
        tmp = head
        while tmp:
            len += 1
            tmp = tmp.next
        # 给原链表添加一个头部，方便操作
        new = ListNode(0)
        new.next = head
        # 两个操作指针
        pre = new
        p = pre.next
        for i in range(len-n):
            pre = pre.next
            p = pre.next
        # 删除指定点
        pre.next = p.next
        return new.next


a = Solution()
l1 = ListNode(1)
print(l1, 1)