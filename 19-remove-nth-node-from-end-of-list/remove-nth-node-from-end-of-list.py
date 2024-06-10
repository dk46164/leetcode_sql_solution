# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        
        fast_pnt = head
        slow_pnt = head

        while n:
            fast_pnt = fast_pnt.next
            n-=1
        
        if fast_pnt is None:
            return head.next
        
        while fast_pnt.next:
            slow_pnt = slow_pnt.next
            fast_pnt = fast_pnt.next


        # swap node values
        tmp = slow_pnt.next
        slow_pnt.next =  slow_pnt.next.next
        tmp  = None

        return head

        

        