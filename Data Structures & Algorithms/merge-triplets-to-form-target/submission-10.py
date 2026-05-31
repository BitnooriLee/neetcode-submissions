class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        if len(triplets) == 1:
            if triplets[0] == target:
                return True
            else: return False 

        triplets.sort()
        i = 0 
        a,b,c = target
        while (i < len(triplets) and a >= triplets[i][0]):
            i+= 1 
        triplets = triplets[:i]

        triplets.sort(key= lambda x:x[1])

        j = 0 
        while (j < len(triplets) and b >= triplets[j][1]):
            j+= 1 
        triplets = triplets[:j]

        triplets.sort(key= lambda x:x[2])

        k = 0 
        while (k < len(triplets) and c >= triplets[k][2]):
            k+= 1 
        triplets = triplets[:k]

        if len(triplets) < 1:
            return False

        if max(triplets[i][0] for i in range(len(triplets))) == a  and max(triplets[i][1] for i in range(len(triplets))) == b and max(triplets[i][2] for i in range(len(triplets))) == c:
            return True
        return False