# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists: return None
        if len(lists) == 1:
            return lists[0]

        def merge(l1,l2):
            dummy = ListNode(0)
            head = dummy

            cur1, cur2 =l1, l2
            while(cur1 and cur2):
                if cur1.val <= cur2.val:
                    head.next = cur1 
                    cur1 = cur1.next  
                else:
                    head.next = cur2
                    cur2 = cur2.next
                head = head.next 
            if cur1:
                head.next = cur1
            if cur2:
                head.next = cur2 
            return dummy.next

        def mergeresult(output):
            if len(output) == 1:
                return output[0]
            res = []
            if len(output)%2 == 0:
                end = len(output) 
            else:
                end = len(output)-1 
            for i in range(0,end,2):
                res.append(merge(output[i], output[i+1]))
            if end == len(output)-1:
                res.append(output[-1])
            return mergeresult(res)


        return mergeresult(lists)

        
            

        