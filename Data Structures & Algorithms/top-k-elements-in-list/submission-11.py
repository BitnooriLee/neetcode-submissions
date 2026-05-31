from collections import defaultdict
import heapq 
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dic = defaultdict(int)
        for num in nums:
            dic[num]+= 1 
        
        q = []

        for ky in dic:
            heapq.heappush(q,(dic[ky],ky))
            if len(q) > k:
                heapq.heappop(q)
        result = []
      
        while q:
            result.append(heapq.heappop(q)[1])
        
        return result

         
            

        