class TimeMap:

    def __init__(self):
        self.dic = defaultdict(list)
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.dic[key].append((timestamp, value))
        

    def get(self, key: str, timestamp: int) -> str:
        res = ""
        values = self.dic.get(key,[])

        l,r = 0, len(values)-1 
        while(l<=r):
            m = r + (l-r)//2 
            if values[m][0] <= timestamp:
                res = values[m][1]
                l = m +1 
            else:
                r = m -1 
        return res
        
