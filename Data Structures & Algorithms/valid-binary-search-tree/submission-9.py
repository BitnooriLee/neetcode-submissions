# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def validBST(l, node ,r):
            if not node:
                return True
            if l < node.val < r:
                return validBST(l, node.left, node.val) and validBST( node.val, node.right, r)
            else:
                return False
        return validBST(-float("Inf"), root, float("Inf"))

