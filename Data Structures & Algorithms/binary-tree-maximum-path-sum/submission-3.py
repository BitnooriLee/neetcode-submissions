# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        res = float("-inf")
  
        def dfs(node):
            nonlocal res 
            if not node:
                return 0

            l = max(0, dfs(node.left))
            r = max(0, dfs(node.right))
            res = max(res, node.val + l + r) # 음수면 안씀 
            return node.val + max(l,r) #부모 노드로는 왼쪽 오른쪽 중 하나만 선택 가능 

        dfs(root)

        return res 

        