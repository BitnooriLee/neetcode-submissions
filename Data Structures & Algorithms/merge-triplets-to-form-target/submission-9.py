class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
       
        good = set()
        for i in range(len(triplets)):
            a,b,c = triplets[i]
            if a > target[0] or b > target[1] or c > target[2]:
                continue
            for i,v in enumerate(triplets[i]):
                if v == target[i]:
                    good.add(i)
        return len(good) == 3
            

        
        



        