# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res  = []
        lvl = 0
        if root:
            que = [[root]]
            while que:
                t = que.pop(0)
                te_n = []
                te_v = []
                while t:
                    t1 = t.pop(0)
                    if t1:
                        te_v.append(t1.val)
                        te_n.append(t1.left)
                        te_n.append(t1.right)
                if te_n:
                    que.append(te_n)
                
                if te_v and lvl%2:
                    res.append(te_v[::-1])
                if te_v and not lvl%2:
                    res.append(te_v)
                
                lvl+=1

        return res




        