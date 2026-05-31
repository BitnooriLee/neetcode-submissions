class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        carry = 1
    
        for i in range(len(digits)-1,-1,-1):
            if digits[i]+carry == 10:
                digits[i] = 0 
            else:
                digits[i] += 1 
                carry = 0 
                break

        if carry == 0:
            return digits
        else:
            print(digits)
            return [1] + digits
                
        