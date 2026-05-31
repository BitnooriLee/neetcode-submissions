# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if not preorder or not inorder:
            return 
        mid = preorder[0]
        mid_idx = inorder.index(mid)
        root = TreeNode(mid)
        root.left = self.buildTree(preorder[1:mid_idx+1], inorder[:mid_idx])
        root.right = self.buildTree(preorder[mid_idx+1:], inorder[mid_idx+1:])
        
        return root 

        