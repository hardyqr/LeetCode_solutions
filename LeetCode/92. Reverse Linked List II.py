# Fangyu
# 12/2/2016

# 对于listnode的操作

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reverseBetween(self, head, m, n):
        """
        :type head: ListNode
        :type m: int
        :type n: int
        :rtype: ListNode
        """
        if not head or not head.next:return head
        count=1
        tmp=head
        before=None
        while count<m:
            before=tmp
            tmp=tmp.next
            count+=1
