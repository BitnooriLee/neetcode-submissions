# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.maxSum = float("-inf")

        def travel(node):
            
            if not node:
                return 0
            l = max(0, travel(node.left))
            r = max(0, travel(node.right))
           
            self.maxSum = max(self.maxSum, node.val+l+r)
            return node.val + max(l,r) #부모한테는 현재값하고 왼쪽 또는 오른쪽 하나만 전달할 수 있다 그래야 이어이지니까 
        travel(root)

        return self.maxSum
            
        
        