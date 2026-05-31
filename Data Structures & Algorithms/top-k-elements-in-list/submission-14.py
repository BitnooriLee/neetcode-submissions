class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        if len(nums) == 1:
            return nums
        minh = []
        cnt = Counter(nums)
        for ky,v in cnt.items():
            heapq.heappush(minh, (v,ky))
            while len(minh) > k:
                heapq.heappop(minh)

        return [pair[1] for pair in minh]

  