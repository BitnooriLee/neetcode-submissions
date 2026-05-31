# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        #반자르고 
        slow, fast = head, head
        while (fast and fast.next):
            slow= slow.next
            fast = fast.next.next 
        second = slow.next
        slow.next = None 
        #reverse
        prev, cur = None, second
        while(cur):
            tmp = cur.next
            cur.next = prev
            prev = cur
            cur = tmp 

        #alter in-space 
        first, second = head, prev 
        while(second):
            tmp = first.next 
            first.next = second
            tmp2 = second.next
            second.next = tmp 

            first = tmp
            second = tmp2 
        

        
        
        
        