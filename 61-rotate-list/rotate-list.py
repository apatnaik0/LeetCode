# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head:
            return None
        l = 1
        temp = head
        while temp.next:
            temp = temp.next
            l += 1
        temp.next = head
        k = k % l
        rot = l - k

        temp = head
        for i in range(rot-1):
            temp = temp.next
        
        newhead = temp.next
        temp.next = None
        return newhead
