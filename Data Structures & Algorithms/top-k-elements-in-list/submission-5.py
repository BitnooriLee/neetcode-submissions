class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dic = Counter(nums)
        output = []
        for key,v in dic.items():
            heapq.heappush(output,(v,key))
            if len(output) > k:
                heapq.heappop(output)
    
        res = []
        for _ in range(k):
            res.append(heapq.heappop(output)[1])
            
        return res


        