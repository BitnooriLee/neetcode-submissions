# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        def isValid(left_max, root, right_min):
            if not root:
                return True
            if left_max < root.val <right_min:
                return isValid(left_max, root.left, root.val) and isValid(root.val, root.right, right_min) 
            else:
                return False
        return isValid(-float("inf"), root, float("inf"))