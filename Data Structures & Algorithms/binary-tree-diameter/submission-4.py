# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        res = 0 

        def dfs(node): #각 노드에서 가장 긴 길이 왼,오 중 
            nonlocal res 
            if not node:
                return 0

            l,r = dfs(node.left), dfs(node.right)
            res = max(res, l+r) # 왼,오 둘다 합친게 거리 
            return max(r,l)+1 

        dfs(root)

        return res
        