# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        c = 0
        dummy = ListNode(-1)
        cur = dummy
        while l1 or l2 or c:
            s = 0
            if l1:
                s += l1.val
            if l2:
                s += l2.val
            s += c
            node = ListNode(s%10)
            c = s//10
            cur.next = node
            cur = node
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next
        return dummy.next
