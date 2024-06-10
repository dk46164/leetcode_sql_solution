# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:

        #result root node
        res_head = cur = ListNode(0)      
        cry = 0
        while l1 or l2 or cry:
            if l1:
                cry+=l1.val
                l1 = l1.next
            if l2:
                cry+=l2.val
                l2 = l2.next
            
            cur.next = ListNode(cry%10)
            cur = cur.next
            cry = cry//10

        return res_head.next 



        