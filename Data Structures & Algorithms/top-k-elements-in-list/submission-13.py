class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        if len(nums) == 1:
            return nums
        cnt = Counter(nums)

        minh = []

        for i in cnt.keys():
            heapq.heappush(minh, (cnt[i],i))
            while len(minh)>k:
                heapq.heappop(minh)

        output = []
        for i in range(k):
            v,i = heapq.heappop(minh)
            output.append(i)

        return output[::-1]
        


#time: O(n)-> O(nlogn) heappush logn 
#space: O(n)