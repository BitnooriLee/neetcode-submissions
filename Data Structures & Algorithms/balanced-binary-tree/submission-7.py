# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def dfs(node): #heights를 리턴. isBalanced 는 True, False리턴 
            if not node:
                return 0
            l = dfs(node.left)
            r = dfs(node.right)
            return max(l,r)+1
        if not root:
            return True
        if abs(dfs(root.left) - dfs(root.right)) <=1:
            return self.isBalanced(root.left) and self.isBalanced(root.right)
        else:
            return False
        

        


        