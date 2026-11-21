class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        cnt = defaultdict(int)
        for n in nums:
            cnt[n] += 1 
        output = []
        h = []
        for key in cnt.keys():
            heapq.heappush(h, (cnt[key],key))
            if len(h) > k:
                heapq.heappop(h)

        while h:     
            output.append(heapq.heappop(h)[1])
        
        return output