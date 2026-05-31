# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        res = float("-inf")

        def dfs(node):
            nonlocal res
            if not node:
                return 0 

            l = max(0,dfs(node.left))
            r = max(0, dfs(node.right))
            res = max(res, node.val+l+r)
            return node.val + max(r,l)

        dfs(root)

        return res 

        