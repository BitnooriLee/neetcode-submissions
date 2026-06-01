# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        self.answer = None
        self.k = k 
        def traversal(node):
            if not node:
                return 
            traversal(node.left)
            self.k -= 1 
            if self.k == 0:
                self.answer = node.val
                return
            
            traversal(node.right)
        traversal(root)

        return self.answer
        