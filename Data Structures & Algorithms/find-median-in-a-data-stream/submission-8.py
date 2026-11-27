class MedianFinder:

    def __init__(self):
        self.low = []
        self.high = []
        self.total = 0
        

    def addNum(self, num: int) -> None:
        heapq.heappush(self.low, -num) # low에 먼저 넣음
        _num = heapq.heappop(self.low)
        heapq.heappush(self.high, -_num) # low가 1개 늘었으니까 그 최대를 high에 

        if len(self.low) < len(self.high):
            _num = heapq.heappop(self.high)
            heapq.heappush(self.low, -_num)
        self.total += 1

    def findMedian(self) -> float:
        if self.total%2 == 0:
           return (-self.low[0]+self.high[0])/2.0
        else:
            return -self.low[0]
        
        