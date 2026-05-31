class CountSquares:

    def __init__(self):
        self.dic = defaultdict(int)
        

    def add(self, point: List[int]) -> None:
        self.dic[(point[0], point[1])] += 1

    def count(self, point: List[int]) -> int:
        x,y = point 
        res = 0 
        for (xx, ny), c in self.dic.items():
            if xx != x or ny == y:
                    continue

            d = ny - y  # 변 길이(부호 포함)

            # 오른쪽
            res += c * self.dic.get((x + d, y),0) * self.dic.get((x + d, ny),0)
            # 왼쪽
            res += c * self.dic.get((x - d, y),0) * self.dic.get((x - d, ny),0)

        return res
