class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        if len(digits) == 1:
            return [1,0] if digits[0]==9 else [digits[0]+1]

        res = 0 
        power = 1 
        for i in range(len(digits)-1,-1,-1):
            res += digits[i]*power
            power *= 10 
        res += 1 
        output = []
        while(res>0):
            d = res%10
            output.append(d)
            res = res//10
        #output.append(res)

        return output[::-1]



        