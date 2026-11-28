# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        #preorder, add @, null "null"
        output = []
        def preorder(node):
            if not node:
                output.append("null")
                return node
            output.append(str(node.val))
            preorder(node.left)
            preorder(node.right)
        preorder(root)
        return "@".join(output)
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        #"1@2@3@null..."
        q = deque(data.split("@"))

        def dfs():
            st = q.popleft()
            if st == "null":
                return None
            root = TreeNode(int(st))
            root.left = dfs()
            root.right = dfs()
            return root

        return dfs()
        









