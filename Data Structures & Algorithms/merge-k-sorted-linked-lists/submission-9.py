# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists:
            return None
        _lists = lists
        while(len(_lists)>1):
            merged = []
            for i in range(0,len(_lists),2):
                tmp = ListNode()
                tail = tmp
                l1 = _lists[i]
                l2 = _lists[i+1] if i+1 < len(_lists) else None #홀수인 경우 처리 
                while (l1 and l2):
                    if l1.val > l2.val:
                        tail.next = l2
                        l2 = l2.next
                    else:
                        tail.next = l1
                        l1 = l1.next
                    tail = tail.next
                if l1:
                    tail.next = l1
                if l2:
                    tail.next = l2
                merged.append(tmp.next)
            _lists = merged

        return _lists[0]
        