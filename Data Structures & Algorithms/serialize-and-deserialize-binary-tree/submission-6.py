# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        res = []
        if not root:
            return ""

        def bfs(cur):
            nonlocal res 
            if not cur:
                res.append("null")
                return
            else:
                res.append(str(cur.val))
                bfs(cur.left)
                bfs(cur.right)
        bfs(root)
        return ",".join(res)
        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        if not data:
            return None
       
        sts = iter(data.split(","))
        
        def dfs():
            st = next(sts)
            if st == "null":
                return None
            root = TreeNode(int(st))
            root.left = dfs()
            root.right = dfs()
            return root
        return dfs()


