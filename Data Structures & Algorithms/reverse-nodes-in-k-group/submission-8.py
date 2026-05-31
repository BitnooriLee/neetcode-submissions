# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = ListNode(0,head)
        group_prev = dummy 

        def findK(node,k):
            while(node and k > 0):
                node = node.next
                k-=1
            return node

        while(True):
            kth = findK(group_prev, k)
            if not kth:
                break
            group_nxt = kth.next 

            prev, cur = kth.next, group_prev.next 

            while(cur!= group_nxt):
                tmp = cur.next 
                cur.next = prev 
                prev = cur 
                cur = tmp

            tmp = group_prev.next #리버스를 위헤 cur가 정지한 곳 
            group_prev.next = kth # 다음 그룹의 맨 앞 
            group_prev = tmp 

        return dummy.next 
        
            