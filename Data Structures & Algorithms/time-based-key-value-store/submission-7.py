class TimeMap:

    def __init__(self):
        self.dic = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.dic[key].append((timestamp,value))


    def get(self, key: str, timestamp: int) -> str:
        if not key in self.dic:
            return "" 

        i,j = 0, len(self.dic[key])-1
        while(i<=j):
            m = i + (j-i)//2 
            if self.dic[key][m][0] == timestamp:
                return self.dic[key][m][1]
            elif self.dic[key][m][0] < timestamp:
                i = m + 1 
            else:
                j = m - 1 
        return self.dic[key][i-1][1] if i-1 >= 0 else ""



        
