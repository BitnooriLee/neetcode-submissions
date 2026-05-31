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
        idx = inorder.index(mid)
        left = idx - 1
        root = TreeNode(mid)
        root.left = self.buildTree(preorder[1:left+2],inorder[:idx])
        root.right = self.buildTree(preorder[left+2:],inorder[idx+1:])

        return root 
        
        