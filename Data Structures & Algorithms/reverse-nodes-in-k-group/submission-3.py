# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = ListNode(0,head)
        groupprev = dummy 

        def findKth(cur,k):
            while(cur and k > 0):
                cur = cur.next 
                k -= 1 
            return cur 

        while True:
            kth = findKth(groupprev,k)
            if not kth:
                break 
            groupnext = kth.next

            # reverse 
            prev, cur = kth.next, groupprev.next # 다음 그룹과 연결해줌, groupnext하고 groupprev는 가만히 있음 
            while(cur != groupnext):
                tmp = cur.next
                cur.next = prev
                prev = cur 
                cur = tmp 
        
            tmp = groupprev.next 
            groupprev.next = kth # 맨앞 연결 
            groupprev = tmp 

        return dummy.next
        
        