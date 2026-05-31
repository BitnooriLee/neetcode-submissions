# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        #preorder BFS
        if not root:
            return ""
        q = deque([root])
        res = []
        while q:
            cur = q.popleft()
            if not cur:
                res.append("null")
            else:
                res.append(str(cur.val))
                q.append(cur.left)
                q.append(cur.right) 
        return ",".join(res)

        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        if not data:
            return None

        nodes = data.split(",")
        root = TreeNode(int(nodes[0])) #node.val int 
        q = deque([root])
        idx = 1 

        while q:
            cur = q.popleft()
            if nodes[idx] != "null":
                cur.left = TreeNode(int(nodes[idx]))
                q.append(cur.left)
            idx += 1 
            if nodes[idx] != "null":
                cur.right = TreeNode(int(nodes[idx]))
                q.append(cur.right)
            idx += 1 

        return root 
        

