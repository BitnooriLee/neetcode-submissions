class CountSquares:

    def __init__(self):
        self.cnt = defaultdict(int)
        self.px = defaultdict(set)
        

    def add(self, point: List[int]) -> None:
        self.cnt[(point[0],point[1])] += 1 
        self.px[point[0]].add(point[1])

    def count(self, point: List[int]) -> int:
        x,y = point 
        res = 0 
        for y2 in self.px[x]:
            if y == y2:
                continue

            d = y2-y 
            
            x2 = x + d 
            res+= self.cnt[(x,y2)]*self.cnt[(x2,y)]*self.cnt[(x2,y2)]
            
            x2 = x - d 
            res+= self.cnt[(x,y2)]*self.cnt[(x2,y)]*self.cnt[(x2,y2)]


        return res
              

        
