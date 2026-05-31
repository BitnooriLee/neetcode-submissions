# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def helper(l,cur,r):
            if not cur:
                return True
            if l < cur.val < r:
                return helper(cur.val,cur.right,r) and helper(l,cur.left,cur.val)
            else:
                return False

        return helper(float("-inf"), root, float("inf"))
