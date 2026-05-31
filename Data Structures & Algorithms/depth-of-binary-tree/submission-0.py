# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0 
        def dep(node, ans):
            if not node:
                return ans

            return max(dep(node.left, ans+1), dep(node.right, ans+1))

        return dep(root,0)
