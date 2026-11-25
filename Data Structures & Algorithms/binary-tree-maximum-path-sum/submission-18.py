# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        res = - float("inf")
        
        def maxSum(node): # 요 노드를 꼭지점으로 포함할때의 최대
            nonlocal res 
            if not node:
                return 0
            l = max(0,maxSum(node.left))
            r = max(0,maxSum(node.right)) 
            res = max(res,max(node.val, node.val+l+r))

            return node.val + max(l,r) #한 가지만, 아니면 분기 생김 

        maxSum(root)

        return res
        
        