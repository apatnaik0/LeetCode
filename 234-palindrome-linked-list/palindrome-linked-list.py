# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        slow = head
        fast = head
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
        
        new_head = slow.next
        prev = None
        while new_head:
            front = new_head.next
            new_head.next = prev
            prev = new_head
            new_head = front
        
        while prev:
            if prev.val != head.val:
                return False
            prev = prev.next
            head = head.next
        return True
        



        