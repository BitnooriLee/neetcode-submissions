class MedianFinder:

    def __init__(self):
        self.lh = []
        self.rh = []
        

    def addNum(self, num: int) -> None:
        heapq.heappush(self.rh, num)

        if self.lh and self.rh and self.rh[0] < -self.lh[0]:
            tmp = heapq.heappop(self.rh)
            heapq.heappush(self.lh, -tmp)

        #balance 
        if len(self.rh) - len(self.lh) > 1:
            tmp = heapq.heappop(self.rh)
            heapq.heappush(self.lh, -tmp)
        
        if len(self.rh) < len(self.lh)  :
            tmp = heapq.heappop(self.lh)
            heapq.heappush(self.rh, -tmp)



        

    def findMedian(self) -> float:
        if len(self.lh) == len(self.rh): #even 
            return (-self.lh[0] + self.rh[0])/2.0
        else:
            return self.rh[0]

        