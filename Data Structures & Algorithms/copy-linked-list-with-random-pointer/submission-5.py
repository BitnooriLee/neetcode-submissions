"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        oldNodeToCopy = {None:None}
        cur = head
        while(cur):
            copy = Node(cur.val)
            oldNodeToCopy[cur] = copy
            cur = cur.next

        cur = head

        while(cur):
            copy = oldNodeToCopy[cur]
            copy.next = oldNodeToCopy[cur.next]
            copy.random = oldNodeToCopy[cur.random]
            cur = cur.next 

        return oldNodeToCopy[head]

        
            
        