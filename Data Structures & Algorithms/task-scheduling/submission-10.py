class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        h = [-c for c in Counter(tasks).values()]
        heapq.heapify(h)

        q = deque()
        t = 0 
        while h or q:
            t += 1 
            while q and q[0][1] <= t:
                heapq.heappush(h, q.popleft()[0])
            if h:
                remain = heapq.heappop(h) +1 
                if remain != 0:
                    q.append((remain, t+n+1))
           
            

        return t
      