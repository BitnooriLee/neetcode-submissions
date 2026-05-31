# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists:
            return None         
        if len(lists) ==1:
            return lists[0]
        def merge(l1,l2):
            dummy = ListNode(0)
            cur = dummy
            while (l1 and l2):
                if l1.val < l2.val:
                    cur.next = ListNode(l1.val)
                    l1 = l1.next
                else:
                    cur.next = ListNode(l2.val)
                    l2 = l2.next
                cur = cur.next
            if l1:
                cur.next = l1
            if l2:
                cur.next = l2
            return dummy.next
  
        k = len(lists)
        interval = 1 
        while(interval<k):
            for i in range(0, k-interval, interval):
                lists[i] = merge(lists[i], lists[i+interval])
            interval = interval*2 
            
        return lists[0]



        