# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(-1)
        curr = dummy
        carry = 0
        while l1 or l2 or carry:
            s = 0
            if l1:
                s += l1.val
            if l2:
                s += l2.val
            s += carry
            val = ListNode(s%10)
            curr.next = val
            curr = val
            carry = s//10
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next
        return dummy.next
        