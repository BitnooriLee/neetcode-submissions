# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        res = -float("inf")

        def findMax(node):
            nonlocal res 
            if not node:
                return 0
            left_max = findMax(node.left)
            right_max = findMax(node.right)
            cur_max = node.val + max(left_max, 0) + max(right_max, 0)

            res = max(res,cur_max)
            return node.val + max(0, max(left_max,right_max))

        
        findMax(root)
        return res 