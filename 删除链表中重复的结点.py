#在一个排序的链表中，存在重复的结点，请删除该链表中重复的结点，重复的结点不保留，返回链表头指针。 例如，链表1->2->3->3->4->4->5 处理后为 1->2->5

# -*- coding:utf-8 -*-
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteDuplication(self,pHead):
        if pHead is None or pHead.next is None:  
            return pHead
        head1=pHead.next
        if head1.val != pHead.val:
            pHead.next = self.deleteDuplication(pHead.next)    #递归
        else:
            while pHead.val == head1.val and head1.next is not None:   #还剩下至少3个结点，且前两个结点值相等，如4->4->5, 4->4>-4
                head1 = head1.next     #4->5,4->4
            if head1.val != pHead.val:
                pHead=self.deleteDuplication(head1)   #递归
            else:
                return None       #如果剩下的两个值相等则，返回None
        return pHead
