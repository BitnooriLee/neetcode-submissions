class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        h = [-c for c in Counter(tasks).values()]
        heapq.heapify(h)
        q = deque() # remain_count, time can start 

        time = 0 
        
        while h or q:
            time+=1 

            while q and q[0][1] <= time:
                heapq.heappush(h, q.popleft()[0])
            if h:
                remain = heapq.heappop(h) + 1 # 음수 + 1 즉 1개 줄인것 
                if remain != 0:
                    q.append((remain, time+n+1))

        return time 


        