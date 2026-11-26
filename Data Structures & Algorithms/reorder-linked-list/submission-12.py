# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # cut at half 
        slow, fast = head, head
        while(fast and fast.next):
            slow = slow.next 
            fast = fast.next.next 
        second = slow.next
        slow.next = None 
        # reverse till half 
        prev, cur = None, second # 여기가 매우 헷갈림. second (뒤집으려는 ll, cur 포인터)
        while(cur):
            tmp = cur.next 
            cur.next = prev 
            prev = cur 
            cur = tmp
        # merge 
        second = prev 
        first = head    

        while(second):
            tmp = first.next
            first.next = second
            tmp2 = second.next
            second.next = tmp

            first = tmp
            second = tmp2 
        
        