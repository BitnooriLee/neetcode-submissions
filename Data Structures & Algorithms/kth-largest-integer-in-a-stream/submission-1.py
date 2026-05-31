class KthLargest:
    # adding new val -> sort everytime -> cost 
    # hp, k fixed 
    # kth largest, size k hp[0]
    #3th 
    #10 9 8 8-9-10 
    # 10 9 8 11 8-9-10-11 pop -> 9-10-11 
    def __init__(self, k: int, nums: List[int]):
        self.h = []
        self.k = k
        for num in nums:
            heapq.heappush(self.h, num)

        while(len(self.h)>k):
            heapq.heappop(self.h)

    def add(self, val: int) -> int:
        heapq.heappush(self.h,val)
        if (len(self.h)>self.k):
            heapq.heappop(self.h)
        return self.h[0]        
