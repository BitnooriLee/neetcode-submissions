class Solution:
    def longestPalindrome(self, s: str) -> str:
        def isPal(i,j):
            while(i<j):
                if s[i] != s[j]:
                    return False
                i += 1 
                j -= 1 
            return True 

        m = 0
        mr,ml = 0,0

        for r in range(len(s)-1,-1,-1):
            l = 0
            while(l<r):
                if isPal(l,r):
                    if m < r - l + 1:
                        m = r - l + 1
                        mr,ml = r,l
                l += 1 
                
        return s[ml:mr+1]
            

                    
                

                

        