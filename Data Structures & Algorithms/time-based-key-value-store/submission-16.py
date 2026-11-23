class TimeMap:

    def __init__(self):
        self.dic = defaultdict(list)
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.dic[key].append((timestamp,value))
        
    def get(self, key: str, timestamp: int) -> str:
        if key not in self.dic:
            return ""
        def get_largest_t(key, timestamp):
            l,r = 0, len(self.dic[key])
            while(l<r):
                m = (r - l)//2 + l 
                if self.dic[key][m][0] > timestamp:
                    r = m
                else:
                    l = m + 1
            return l
        l = get_largest_t(key, timestamp)

        return self.dic[key][l-1][1] if l > 0 else ""

        
