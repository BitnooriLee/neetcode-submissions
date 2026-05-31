class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dic = collections.Counter(nums)
        fre = []
        output = []

        for n,freq in dic.items():
            heapq.heappush(fre, (-freq,n))
        
        for _ in range(k):
            output.append(heapq.heappop(fre)[1])

        return output
        


        
            
        
        
                

        