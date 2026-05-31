# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        #bfs...
        if not root:
            return []
        output = []
        def bfs(node):
            q=deque([node])
            while q:
                l = len(q)
                
                for i in range(l):
                    cur = q.popleft()
                    if i == l-1:
                        output.append(cur.val)
                    if cur.left:
                        q.append(cur.left)
                    if cur.right:
                        q.append(cur.right)
            return output

        bfs(root)
        return output
                        

        