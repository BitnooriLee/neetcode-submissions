# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if len(lists)==0:
            return None
        if len(lists)==1:
            return lists[0]

        def merge(list1, list2):
            dummy = ListNode(0)
            cur = dummy
            while(list1 and list2):
                if list1.val < list2.val:
                    cur.next = ListNode(list1.val)
                    list1 = list1.next 
                else:
                    cur.next = ListNode(list2.val)
                    list2 = list2.next 
                cur = cur.next 
            if list1:
                cur.next =list1
            if list2:
                cur.next =list2
            return dummy.next
        k = len(lists)
        interval = 1 
        while(interval < k):
            for i in range(0,k-interval, interval):
                lists[i] = merge(lists[i], lists[i+interval])
            interval*= 2 
        return lists[0]
        
        