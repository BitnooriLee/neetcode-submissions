class TimeMap:

    def __init__(self):
        self.dic = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.dic[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.dic:
            return ""

        n = len(self.dic[key])
        l,r = 0, n 
        while(l<r):
            m = l + (r-l)//2
            if self.dic[key][m][0] <= timestamp:
                l = m + 1 
            else:
                r = m 
        #l은 False의 첫 위치 
        if l > 0:
            return self.dic[key][l-1][1] 
        else:
            return ""
        
