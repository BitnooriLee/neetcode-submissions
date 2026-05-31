class MedianFinder:

    def __init__(self):
        self.largeh = []
        self.smallh = []
        

    def addNum(self, num: int) -> None:
        heapq.heappush(self.largeh, num)
        #make sure smallest in largeh >= largest in smallh 
        # smallh largeh shouldn't be None
        if self.largeh and self.smallh and self.largeh[0] < -self.smallh[0]:
            tmp = heapq.heappop(self.largeh)
            heapq.heappush(self.smallh, -tmp)

        #balance to be median 
        #len(largeh) - len(smallh) < 2
        #len(largeh) >= len(smallh)

        if len(self.largeh) - len(self.smallh) > 1:
            tmp = heapq.heappop(self.largeh)
            heapq.heappush(self.smallh, -tmp)

        if len(self.smallh) > len(self.largeh):
            tmp = heapq.heappop(self.smallh)
            heapq.heappush(self.largeh, -tmp)

        
        

    def findMedian(self) -> float:
        if len(self.largeh) > len(self.smallh):
            
            return self.largeh[0]
        else:
            return (self.largeh[0]- self.smallh[0])/2.0
        
        
        