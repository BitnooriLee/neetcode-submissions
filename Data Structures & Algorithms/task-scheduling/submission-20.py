class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        cnts = defaultdict(int)
        q = deque() # - 남은수, 다시 이 task를 할 수 있는 시간  
        for task in tasks:
            cnts[task] += 1
        h = []
        for cnt in cnts.values():
            heapq.heappush(h,-cnt)
        time = 0 
        while q or h:
            time += 1
            while q and time >= q[0][1]:
                heapq.heappush(h, q.popleft()[0])           
            if h:
                remain = heapq.heappop(h) + 1 
                if remain < 0:
                    q.append((remain, time+1+n))

        return time 
