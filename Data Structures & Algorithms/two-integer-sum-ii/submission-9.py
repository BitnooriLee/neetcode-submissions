class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:

        for i in range(len(numbers)):
            l,r = i+1, len(numbers)-1
            find = target - numbers[i]
            while(l<=r):
                m = (r-l)//2 + l
                if find == numbers[m]:
                    return [i+1,m+1]
                elif numbers[m] < find:
                    l = m+1
                else:
                    r = m-1
        return [-1,-1]
            


        