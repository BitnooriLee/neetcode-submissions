class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        m,n = len(nums1), len(nums2)
        if m > n :
            nums1,nums2 = nums2, nums1
            m,n = n,m

        A, B = nums1, nums2

        half = (m+n)//2 

        l,r = 0, m-1
        while True:
            i = (l+ (r-l)//2)
            j = half-i- 2 # 여기도 주의 

            Aleft = A[i] if i >=0 else float("-inf")
            Aright = A[i+1] if i+1 < m else float("inf")
            Bleft = B[j] if j >=0 else float("-inf")
            Bright =  B[j+1] if j+1 < n else float("inf")
            #return 조건 
            if Aleft <= Bright and Aright >= Bleft:
                if (m+n)%2 == 0:
                    return (max(Aleft, Bleft) + min(Aright, Bright))/2
                else:
                    return min(Aright,Bright)

            if Aleft > Bright:
                r = i -1 
            if Bleft > Aright:
                l = i + 1 

        
        