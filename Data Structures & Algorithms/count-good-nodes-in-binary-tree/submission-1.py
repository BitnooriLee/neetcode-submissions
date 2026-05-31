# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        res = 0
        if not root:
            return 0

        def dfs(node, cur):
            nonlocal res 
            if not node:
                return 
            if cur <= node.val:
                res += 1
                cur = node.val 
            dfs(node.left,cur)
            dfs(node.right,cur)

        dfs(root, root.val)
        return res 

        