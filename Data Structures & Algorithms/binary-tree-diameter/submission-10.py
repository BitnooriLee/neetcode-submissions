# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        res = 0 

        def dia(node):
            nonlocal res 
            if not node:
                return 0
            l = dia(node.left)
            r = dia(node.right)
            res = max(res, l+r)
            return max(l,r)+1
        dia(root)
        return res

    
        