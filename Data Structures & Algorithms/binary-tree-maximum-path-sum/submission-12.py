# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        res = float("-inf")

        def path(node):
            nonlocal res 
            if not node:
                return 0
            l = max(0,path(node.left))
            r = max(0,path(node.right))
            res = max(res, node.val + l + r)
            return node.val + max(l,r)

        path(root)

        return res