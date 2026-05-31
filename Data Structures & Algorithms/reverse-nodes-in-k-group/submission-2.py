# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = ListNode(0,head)
        group_prev = dummy 

         
        #  get kth 
        def getKth(cur, k):
            while(cur and k>0):
                cur = cur.next
                k-=1 
            return cur

        # reverse 
        while(True):
            kth = getKth(group_prev,k)
            if not kth:
                break 

            #reverse 
            groupNext = kth.next #kth.next는 prev로 움직일꺼임 그래서 저장해둠 

            prev, cur = kth.next, group_prev.next 
            while(cur != groupNext):
                tmp = cur.next 
                cur.next = prev
                prev = cur
                cur = tmp
            tmp = group_prev.next
            group_prev.next = kth
            group_prev = tmp 
        
        return dummy.next





        