# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def isValid(lb, node, rb):
            if not node:
                return True
            if not (lb < node.val < rb):
                return False
            return isValid(lb, node.left, node.val) and isValid(node.val, node.right, rb)
        
        return isValid(-float("inf"), root, float("inf"))

        