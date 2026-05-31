# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.ans = 0

        def distance(node):
            if not node:
                return 0 
            left = distance(node.left)
            right = distance(node.right)

            #maximum? 
            self.ans = max(self.ans, left+right)
            
            #current distance update
            return 1 + max(left,right)

        distance(root)
        return self.ans

