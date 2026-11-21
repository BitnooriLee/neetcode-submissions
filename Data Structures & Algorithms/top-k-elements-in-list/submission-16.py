class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        cnt = defaultdict(int)
        for n in nums:
            cnt[n] += 1 
        output = []
        h = []
        for key in cnt.keys():
            heapq.heappush(h, (-cnt[key],key))
            
        while (k > 0 and h):
            c_v, c_k = heapq.heappop(h)
            output.append(c_k)
            k -= 1
        
        return output