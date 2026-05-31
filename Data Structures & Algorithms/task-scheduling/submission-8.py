class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        counts = Counter(tasks)
        maxHeap = [-cnt for cnt in counts.values()]
        heapq.heapify(maxHeap) #지금 당장 실행 가능, 몇번 남았는지  

        total = 0
        q = deque() #기다리는 테스크들 (몇번 남았나, 언제 다시 실행가능하냐) 0부터 먼저 실행가능 
        while(maxHeap or q):
            total += 1 #한칸 움직여줘야 함 
            if not maxHeap: #당장 실행 가능한게 없으면
                total = q[0][1] # 이때까지 기다려야함       
            else: 
                cnt = heapq.heappop(maxHeap) + 1 #한번 줄어듬 
                if cnt: #아직 더 실행해야하면 
                    q.append([cnt, total+n])
            if q and q[0][1] == total: #현재 실행 가능한 게 큐에 있으면 앞에서 시간 업뎃했으므로 
                heapq.heappush(maxHeap, q.popleft()[0]) 
        return total 
            