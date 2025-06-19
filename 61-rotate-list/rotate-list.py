# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if head is None or head.next is None:
            return head
        ct = 1
        tail = head
        while tail.next:
            ct+=1
            tail = tail.next
        # print(ct)
        tail.next = head
        end = ct-(k%ct)
        temp = head
        for i in range(end-1):
            # print(temp.val)
            temp = temp.next
            # print(temp.val)
        newhead = temp.next
        temp.next = None
        return newhead
        