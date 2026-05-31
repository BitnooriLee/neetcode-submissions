# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        #return max value
        if not root:
            return 0 
        
        def dfs(node, cur_mx):
            if not node:
                return 0
            if node.val >= cur_mx:
                count = 1 
            else:
                count = 0 
            cur_mx = max(cur_mx, node.val)
            count +=dfs(node.left, cur_mx)
            count += dfs(node.right, cur_mx)
            return count 
        return dfs(root,root.val)
        