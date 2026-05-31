class TimeMap:

    def __init__(self):
        self.dic = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.dic[key].append((timestamp, value))
        
    def get(self, key: str, timestamp: int) -> str:
        if key not in self.dic:
            return ""

        lst = self.dic[key]
        l,r = 0, len(lst) # open 
            
        while(l<r):
            m = l + (r-l)//2
            if lst[m][0] <= timestamp:
                l = m + 1
            else:
                r = m 
        # l 은 첫 False 의 위치 
        if l > 0: 
            return self.dic[key][l-1][1]
        else: 
            return ""

            
        
