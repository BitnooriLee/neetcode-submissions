class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        #k + n(k-1)
        cnt = defaultdict(int)
        maxheap = []
        for task in tasks:
            cnt[task] += 1
        for v in cnt.values():
            heapq.heappush(maxheap, -v)
        
        largest = -heapq.heappop(maxheap)
        c = 0
        while(maxheap and largest == -heapq.heappop(maxheap)):
            c+= 1   
        
        return largest+(largest-1)*n + c if largest+(largest-1)*n + c >= len(tasks) else len(tasks)
        