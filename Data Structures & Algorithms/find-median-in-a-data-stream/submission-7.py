class MedianFinder:

    def __init__(self):
        self.lq = []
        self.rq = []
        
    def addNum(self, num: int) -> None:
      
        heapq.heappush(self.lq, -num)
        if self.lq and self.rq and (-self.lq[0] > self.rq[0]):
            tmp = heapq.heappop(self.lq)
            heapq.heappush(self.rq, -tmp)
        if len(self.lq) - len(self.rq) > 1:
            tmp = heapq.heappop(self.lq)
            heapq.heappush(self.rq, -tmp)
        if len(self.rq) > len(self.lq):
            tmp = heapq.heappop(self.rq)
            heapq.heappush(self.lq, -tmp)
        

    def findMedian(self) -> float:
        total = len(self.lq) + len(self.rq)
   
        if total % 2 == 0:
            return (-self.lq[0]+ self.rq[0])/2.0
        else:
            return -self.lq[0]/1.0
        
        