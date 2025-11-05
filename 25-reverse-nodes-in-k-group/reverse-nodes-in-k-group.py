# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rev(self,head):
        cur = head
        prev = None
        while cur:
            front = cur.next
            cur.next = prev
            prev = cur
            cur = front
        return prev

    def kth(self, head, k):
        while head and k>1:
            head = head.next
            k -= 1
        return head

    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        cur = head
        prev = None
        while cur:
            kth = self.kth(cur,k)
            if not kth:
                if prev:
                    prev.next = cur
                break

            front = kth.next
            kth.next = None
            self.rev(cur)
            if cur == head:
                head = kth
            else:
                prev.next = kth
            prev = cur
            cur = front
        return head
            