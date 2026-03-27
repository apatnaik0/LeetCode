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

        p1 = head

        def rev(head):
            prev = None
            while head:
                front = head.next
                head.next = prev
                prev = head
                head = front
            return prev
        
        p1 = head
        p2 = rev(slow.next)
        slow.next = None

        while p1 and p2:
            if p1.val != p2.val:
                return False
            p1 = p1.next
            p2 = p2.next
        
        return True

        
        