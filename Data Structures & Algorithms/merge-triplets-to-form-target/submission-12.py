class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        if len(triplets) == 1:
            return triplets[0] == target 

        x,y,z = target
        
        triplets.sort()

        i = 0 
        while(i < len(triplets) and triplets[i][0]<=x):
            i += 1 
        triplets = triplets[:i]

        triplets.sort(key = lambda x:x[1])
        i = 0 
        while(i < len(triplets) and triplets[i][1]<=y):
            i += 1 
        triplets = triplets[:i]

        triplets.sort(key = lambda x:x[2])
        i = 0 
        while(i < len(triplets) and triplets[i][2]<=z):
             i += 1 
        triplets = triplets[:i]
        
        if len(triplets) < 1:
            return False 
        if max(triplets[i][0] for i in range(len(triplets)))==x and max(triplets[i][1] for i in range(len(triplets)))==y and max(triplets[i][2] for i in range(len(triplets)))==z:
            return True
        else: return False
        
            

            