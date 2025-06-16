# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:

        if head.next is None:
            return True
        slow = head
        fast = head

        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
        
        rev = slow.next
        prev = None
        while rev.next:
            front = rev.next
            rev.next = prev
            prev = rev
            rev = front
        rev.next = prev

        while rev:
            if rev.val != head.val:
                return False
            rev = rev.next
            head = head.next
        return True
        

        