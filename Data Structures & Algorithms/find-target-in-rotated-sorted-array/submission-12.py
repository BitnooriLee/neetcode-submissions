class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l,r = 0, len(nums)-1 

        while(l<=r): 
            m = l + (r-l)//2

            if nums[m] == target:
                return m 
            # 오른쪽이 정렬 
            elif nums[m] <= nums[r]:
                if nums[m] < target <= nums[r]: # 이미 m이랑 다른거 확인 
                    l = m + 1 
                else:
                    r = m - 1

            # 왼쪽이 정렬 
            else: 
                if nums[l] <= nums[m]:
                    if nums[l] <= target < nums[m]:
                        r = m - 1 
                    else:
                        l = m + 1  

        return -1 




       
        