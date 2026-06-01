# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        if not root:
            return -1
        hp = []
        def traversal(root):
            if not root:
                return 
            traversal(root.left)
            heapq.heappush(hp, root.val)
            traversal(root.right)

        traversal(root)
        for _ in range(k-1):
            heapq.heappop(hp)

        return hp[0]
        