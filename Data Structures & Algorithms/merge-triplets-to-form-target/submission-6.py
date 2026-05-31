class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        if len(triplets) == 1:
            if triplets[0] == target:
                return True
            return False


        one, two, three = target
        l = len(triplets)
        triplets.sort()
        
        i = 0 
        while(i < len(triplets) and triplets[i][0] <= one):
            i+= 1 
        triplets = triplets[:i]     

        triplets.sort(key = lambda x:x[1])       

        i = 0 
        while(i < len(triplets) and triplets[i][1] <= two):
            i+= 1 
        triplets = triplets[:i]    

        triplets.sort(key = lambda x:x[2])     

        i = 0 
        while(i < len(triplets) and triplets[i][2] <= three):
            i+= 1 
        triplets = triplets[:i]  

        if len(triplets) < 1:
            return False
        
        if max(triplets[i][0] for i in range(len(triplets))) == one and  max(triplets[i][1] for i in range(len(triplets))) == two and  max(triplets[i][2] for i in range(len(triplets))) == three:
            return True 
        return False
        