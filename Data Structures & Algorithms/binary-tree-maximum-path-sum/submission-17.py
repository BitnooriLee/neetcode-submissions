# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        res = - float("inf")
        
        def maxSum(node):
            nonlocal res 
            if not node:
                return 0
            l = max(0,maxSum(node.left))
            r = max(0,maxSum(node.right)) 
            res = max(res,max(node.val, node.val+l+r))

            return node.val + max(l,r) #한 가지만 

        maxSum(root)

        return res
        
        