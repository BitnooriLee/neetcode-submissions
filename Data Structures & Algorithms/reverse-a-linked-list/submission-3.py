# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        #two pointer 

        prev, curr = None, head
        
        while curr:
            nxt = curr.next 
            curr.next = prev
            prev = curr
            curr = nxt#curr.next였는데 원래, 이미 prev했으므로 temp variable nxt 써줌 
        return prev