# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rev(self,node):

        prev = None
        while node:
            front = node.next
            node.next = prev
            prev = node
            node = front
        return prev

    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """

        slow = head
        fast = head
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
        
        head1 = head
        head2 = slow.next
        slow.next = None
        head2 = self.rev(head2)

        while head1 and head2:
            front1 = head1.next
            front2 = head2.next
            head1.next = head2
            head2.next = front1
            head1 = front1
            head2 = front2




        