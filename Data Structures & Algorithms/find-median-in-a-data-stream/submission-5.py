class MedianFinder:

    def __init__(self):
        self.maxh = []
        self.minh = []
        

    def addNum(self, num: int) -> None:
        heapq.heappush(self.maxh, -num)
        if self.maxh and self.minh and self.minh[0] < -self.maxh[0]:
            cur = heapq.heappop(self.maxh)
            heapq.heappush(self.minh, -cur)

        if len(self.maxh) - len(self.minh) > 1:
            cur = heapq.heappop(self.maxh)
            heapq.heappush(self.minh, -cur)
        
        if len(self.minh) - len(self.maxh) > 0:
            cur = heapq.heappop(self.minh)
            heapq.heappush(self.maxh, -cur)

        

    def findMedian(self) -> float:
        l = len(self.maxh) + len(self.minh)
        if l%2 == 0:
            return (self.minh[0] - self.maxh[0])/2 
        else:
            return -self.maxh[0]
        
        