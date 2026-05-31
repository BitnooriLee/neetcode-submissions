class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        carry = 0 
        res = []
        digits[-1] += 1
        for i in range(len(digits)-1,-1,-1):
            v = (digits[i]+carry)%10
            carry = (digits[i]+carry)//10
            res.append(v)
        if carry:
            res.append(carry)


        return res[::-1]

            
        