class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        digits.reverse()
        
        carry = 0
        digits[0] +=1
        res = []
        for dig in digits:
            tot = dig+carry
            carry = tot//10
            re = tot%10
            res.append(re)
        if carry:
            res.append(carry)
        res.reverse()
            
        return res