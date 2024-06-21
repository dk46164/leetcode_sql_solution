# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        # get elnght of two ll
        lenb,lena = 0,0

        # init temp
        tempa,tempb = headA,headB
        while tempa:
            lena+=1
            tempa = tempa.next
        
        while tempb:
            lenb+=1
            tempb = tempb.next
        
        # init temp
        tempa,tempb = headA,headB

        if lena>=lenb:
            tmp = lena-lenb
            while tmp:
                tempa = tempa.next
                tmp-=1
        else:
            tmp = lenb-lena
            while tmp:
                tempb = tempb.next
                tmp-=1

        while tempa and tempb:
            if tempa==tempb:
                return tempa
            else:
                tempa = tempa.next
                tempb = tempb.next
        return None




        