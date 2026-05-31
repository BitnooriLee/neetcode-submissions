# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        #level order traversal append when the level finished 
        if not root:
            return []
        output = []

        q= deque([root])

        while q:
            for _ in range(len(q)):
                rightmost = q.popleft()
                if rightmost.left:
                    q.append(rightmost.left)
                if rightmost.right:
                    q.append(rightmost.right)
            output.append(rightmost.val)

        return output
        