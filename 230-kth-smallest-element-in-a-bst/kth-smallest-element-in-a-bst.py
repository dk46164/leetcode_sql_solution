# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        
        # stack init
        stack = []
        curr = root

        # array 
        result = []

        while True:
            # if curr is not none
            if curr:
                stack.append(curr)
                curr = curr.left
            # if all left visited, pop them 
            # put right pointer
            elif stack:
                curr = stack.pop(-1)
                result.append(curr.val)
                curr = curr.right
            else:
                break
        return result[k-1]



        