# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        groupprev = dummy 

        def getKth(cur, k):
            while(cur and k>0):
                cur = cur.next 
                k-=1
            return cur 
       
        while(True):
            kth = getKth(groupprev,k)
            if not kth:
                break 
            # reverse 
            groupNext = kth.next #kth.next 는 prev로 움직일거임 
            
            prev, cur = kth.next, groupprev.next  # none 대신 kth.next 
            while(cur != groupNext):
                tmp = cur.next
                cur.next = prev
                prev = cur 
                cur = tmp

            tmp = groupprev.next 
            groupprev.next = kth
            groupprev = tmp 
        return dummy.next 




        