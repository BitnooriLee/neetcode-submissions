# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        #inorder traversal, output[k]
        # heap? 
        output = [0]
        def traversal(node):
            if not node:
                return 
            traversal(node.left)
            if len(output) > k:
                return 
            output.append(node.val)
            traversal(node.right)

        traversal(root)
        #print(output)
        return output[k]

        