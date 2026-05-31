# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        res = float("-inf")
        
        def dfs(node): # 각 노드까지 올라온 합? 
            nonlocal res
            if not node:
                return 0 
            l = max(0,dfs(node.left))
            r = max(0,dfs(node.right))
            res = max(res, node.val + l + r )
            return node.val + max(l,r)  #부모한테는 현재 값+ 왼쪽 또는 오른쪽만 전달... 위랑 이어지기 위해
        dfs(root)

        return res 