# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = ListNode(0,head)
        groupprev = dummy 

        def findK(cur,k):
            while(cur and k > 0):
                cur= cur.next
                k -= 1
            return cur


        while(True):
            kth = findK(groupprev,k)
            if not kth:
                break
            groupnxt = kth.next

            #reverse 
            prev, cur = kth.next, groupprev.next # 그 다음그룹과 연결해줌 
            
            while(cur!= groupnxt):
                tmp = cur.next 
                cur.next = prev
                prev = cur 
                cur = tmp 
            tmp = groupprev.next 
            groupprev.next = kth # 맨앞 연결
            groupprev = tmp

        return dummy.next



        