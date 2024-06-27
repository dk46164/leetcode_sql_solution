# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        # init var
        head = root

        # loop
        while head:
            if head.val>val:
                head = head.left
            elif head.val<val:
                head = head.right
            else:
                return head
        
        return None
        