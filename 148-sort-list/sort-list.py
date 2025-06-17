# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:

        def middlenode(head):
            slow = head
            fast = head.next
            while fast and fast.next:
                slow = slow.next
                fast = fast.next.next
            return slow

        def merge(lh,rh):
            dummy = ListNode(-1)
            ans = dummy
            while lh and rh:
                if lh.val > rh.val:
                    ans.next = rh
                    rh = rh.next
                else:
                    ans.next = lh
                    lh = lh.next
                ans = ans.next

            if lh:
                ans.next = lh
            if rh:
                ans.next = rh
            return dummy.next

        def ms(head):
            if head is None or head.next is None:
                return head
            middle = middlenode(head)
            righthead = middle.next
            middle.next = None
            lefthead = ms(head)
            righthead = ms(righthead)
            newhead = merge(lefthead,righthead)

            return newhead
        
        return ms(head)
        