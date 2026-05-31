# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        cnt = 0 

        def dfs(node, mx):
            nonlocal cnt
            if not node:
                return 
            if node.val >= mx:
                cnt += 1
                dfs(node.left, node.val)
                dfs(node.right, node.val)
            else:
                dfs(node.left, mx)
                dfs(node.right, mx)

        dfs(root, root.val)

        return cnt
        



    

        