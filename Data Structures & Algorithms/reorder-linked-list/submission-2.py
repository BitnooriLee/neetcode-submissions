# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # find mid 
        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next 

        second = slow.next #beginning of second half 
        slow.next = None #end of fist half 
        pre = None
        # reverse second half
        while second: 
            tmp = second.next 
            second.next = pre 
            pre = second
            second = tmp

        # merge
        first, second = head, pre
        while second: #second is shorter 
            tmp1, tmp2 = first.next, second.next 
            first.next = second
            second.next = tmp1 
            first, second = tmp1, tmp2 
        