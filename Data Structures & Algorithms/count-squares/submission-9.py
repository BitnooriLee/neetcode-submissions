class CountSquares:

    def __init__(self):
        self.dic = defaultdict(int)

    def add(self, point: List[int]) -> None:
        self.dic[(point[0],point[1])] += 1 
        
        

    def count(self, point: List[int]) -> int:
        x,y = point
        res = 0 
        for (nx, ny), c in self.dic.items():
            if nx!=x or ny == y: # x는 같고 y는 다른점. y 길이를 d 로 
                continue 
            d = ny-y

            res+= c * self.dic.get((x-d, ny),0)*self.dic.get((x-d,y),0)
            res+= c * self.dic.get((x+d, ny),0)*self.dic.get((x+d,y),0)
        return res
        
