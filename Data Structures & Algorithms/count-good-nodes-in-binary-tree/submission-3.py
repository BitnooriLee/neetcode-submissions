# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        if not root:
            return 0
        res = 0 
        def dfs(node, max_parent):
            if not node:
                return 
            nonlocal res 
            if node.val >= max_parent:
                res += 1 
            max_parent = max(max_parent, node.val)

            dfs(node.left, max_parent)   
            dfs(node.right, max_parent)
       
        dfs(root, root.val)

        return res 
            
        