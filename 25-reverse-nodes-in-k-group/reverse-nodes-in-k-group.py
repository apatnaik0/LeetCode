# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        def kthnode(head,k):
            temp = head
            while temp and k>1:
                temp = temp.next
                k-=1
            return temp

        def rev(head):
            temp = head
            prev = None
            while temp.next:
                front = temp.next
                temp.next = prev
                prev = temp
                temp = front
            temp.next = prev
            return temp
        
        curr = head
        prev=None
        while curr:
            kth = kthnode(curr,k)
            if not kth:
                if prev:
                    prev.next = curr
                break
            newhead = kth.next
            kth.next = None
            rev(curr)
            if curr == head:
                head = kth
            else:
                prev.next = kth
            prev = curr
            curr = newhead
        return head

            

        