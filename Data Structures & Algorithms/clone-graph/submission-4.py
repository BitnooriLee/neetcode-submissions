"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return 
        oldToCopy = {}
        def dfs(cur): # cur -> copy
            if cur in oldToCopy:
                return oldToCopy[cur]
            
            copy = Node(cur.val)
            oldToCopy[cur] = copy
            
            for nei in cur.neighbors:
                copy.neighbors.append(dfs(nei)) # 새로만든 Node
            return copy

        return dfs(node)      