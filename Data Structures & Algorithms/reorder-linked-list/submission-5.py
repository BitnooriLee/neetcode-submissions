# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        #half까지 
        slow,fast = head,head
        while(fast and fast.next):
            slow = slow.next
            fast = fast.next.next

        second = slow.next  
        slow.next = None 
        # second half reverse 
        prev, cur = None, second
        while(cur):
            tmp = cur.next 
            cur.next = prev
            prev = cur 
            cur = tmp 

        second = prev 
        first = head

        # 한개씩 연결 (새로운거에 연결해도 되나?)
    
        while second:
            tmp = first.next 
            first.next = second
            tmp2 = second.next 
            second.next = tmp 
            #한칸씩 뒤로 
            first = tmp
            second = tmp2

         
