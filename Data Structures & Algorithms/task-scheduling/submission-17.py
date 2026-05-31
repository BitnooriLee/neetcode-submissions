class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        
        mh = [-c for c in Counter(tasks).values()] 
        heapq.heapify(mh)
        q = deque() #이게 핵심, - 남은 수, 가능 시간 

        time = 0 
        while q or mh: 
            time +=1 
            while q and time >= q[0][1]:
                heapq.heappush(mh, q.popleft()[0])
            if mh:
                remain = heapq.heappop(mh) + 1 
                if remain < 0:
                    q.append((remain, time+1+n)) #remain 도 음수임 
                    
        
        return time 

    
        