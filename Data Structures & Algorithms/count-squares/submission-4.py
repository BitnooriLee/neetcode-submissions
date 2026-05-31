class CountSquares:

    def __init__(self):
        self.x_y = defaultdict(set)
        self.cnt = defaultdict(int)

    def add(self, point: List[int]) -> None:
        x,y = point 
        self.x_y[x].add(y)
        self.cnt[(x,y)] += 1 
        

    def count(self, point: List[int]) -> int:
        
        x1,y1 = point 
        res = 0 
        for y2 in self.x_y[x1]:
            if y1 == y2:
                continue 
            
            d = y2 -y1

            x2 = x1-d 
            res+= self.cnt[(x2,y2)]*self.cnt[(x2,y1)]*self.cnt[(x1,y2)]

            x2 = x1+d 
            res+= self.cnt[(x2,y2)]*self.cnt[(x2,y1)]*self.cnt[(x1,y2)]

        return res
        
