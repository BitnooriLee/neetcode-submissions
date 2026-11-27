class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        
        carry = 1
        res = []
        for dig in reversed(digits):
            tot = dig+carry
            carry = tot//10
            re = tot%10
            res.append(re)
        if carry:
            res.append(carry)
            
        return res[::-1]