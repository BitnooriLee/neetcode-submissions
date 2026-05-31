class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        m,n = len(nums1), len(nums2)
        A,B = nums1, nums2 
        if m > n:
            A,B = B,A
            m,n = n,m

        lo,hi = 0,m 
        total = m+n
        half = (total+1)//2 

        while(lo<=hi):
            i = (lo+hi)//2 
            j = half - i 
            Aleft = A[i-1] if i > 0 else float("-inf")
            Aright = A[i] if i < m else float("inf")
            Bleft = B[j-1] if j > 0 else float("-inf")
            Bright = B[j] if j < n else float("inf")

            if Aleft <= Bright and Bleft <= Aright:
                if total%2 == 1:
                    return max(Aleft, Bleft)/1.0
                return (max(Aleft, Bleft) + min(Aright, Bright))/2.0

            if Aleft > Bright:
                hi = i - 1 
            else:
                lo = i + 1 

        return 0.0 
            


        