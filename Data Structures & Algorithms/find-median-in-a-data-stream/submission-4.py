class MedianFinder:

    def __init__(self):
        self.maxh = []
        self.minh = []
        

    def addNum(self, num: int) -> None:
        if self.maxh and num > -self.maxh[0]:
            heapq.heappush(self.minh, num)

        else:
            heapq.heappush(self.maxh, -num)
        
        if len(self.maxh) - len(self.minh) > 1:
            tmp = - heapq.heappop(self.maxh)
            heapq.heappush(self.minh, tmp)
        if len(self.minh) - len(self.maxh) > 0:
            tmp = heapq.heappop(self.minh)
            heapq.heappush(self.maxh, -tmp)


    def findMedian(self) -> float:
        if (len(self.maxh) + len(self.minh))%2 == 0:
            return (-self.maxh[0]+self.minh[0])/2
        else:
            return -self.maxh[0]
        
        
        