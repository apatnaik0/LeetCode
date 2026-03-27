# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if not head.next:
            return None

        cur = head
        nodes = 0

        while cur:
            nodes += 1
            cur = cur.next

        jumps = nodes - n - 1

        if jumps < 0:
            return head.next

        cur = head
        for _ in range(jumps):
            cur = cur.next

        cur.next = cur.next.next

        return head
