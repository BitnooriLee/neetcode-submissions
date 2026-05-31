# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        #BFS 
        output = []
        if not root:
            return []
        def bfs(node):
            q = deque([node])
            while q:
                l = len(q)
                res = []
                for _ in range(l):
                    cur = q.popleft()
                    res.append(cur.val)
                    if cur.left:
                        q.append(cur.left)
                    if cur.right:
                        q.append(cur.right)
                output.append(res)
        bfs(root)

        return output            





        
        