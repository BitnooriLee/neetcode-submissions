class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:

        s,e = 0,len(numbers)-1
        while s < e:
            if numbers[s] == target - numbers[e]:
                return [s+1, e+1]
            elif numbers[s] > target - numbers[e]:
                e -= 1
            else:
                s += 1 

        return [-1,-1]


        