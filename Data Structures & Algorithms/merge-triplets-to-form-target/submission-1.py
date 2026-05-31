class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        can_x,can_y,can_z = False,False,False 
        x,y,z = target 

        for a,b,c in triplets:
            if a > x or b > y or c>z:
                continue
            if a == x:
                can_x = True

            if b == y:
                can_y = True

            if c == z:
                can_z = True

        if can_x and can_y and can_z:
            return True 
        else:
            return False
        