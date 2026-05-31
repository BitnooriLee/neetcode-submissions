# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        #find mid 
        slow,fast = head,head
        while(fast and fast.next):
            slow = slow.next
            fast = fast.next.next 

        #cut l1,
        curr = slow.next #pointer l2 
        slow.next = None #updated head too. 

        # reverse l2 
        prev = None
        while(curr):
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt 
        
        #merge 
        #prev head of reversed l2 
        first = head
        second = prev 
        while(second): #second가 더 짧음
            tmp1 = first.next 
            tmp2 = second.next

            first.next = second
            second.next = tmp1

            first = second.next
            second = tmp2 
        return None





        