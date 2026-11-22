class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        output = []

        for i in range(len(nums)-2):
            if (i > 0 and nums[i-1] == nums[i]):
                continue
            target = -nums[i]
            j,k = i+1,len(nums)-1
            while(j<k):
                if nums[j] + nums[k] == target:
                    output.append([nums[i],nums[j],nums[k]])
                    k-=1
                    j+=1
                    while(j<k and nums[k] == nums[k+1]): 
                        #정답 찾은경우에만, 이미 k-=1을 함, 그래서 사실 nums[k+1]가 전에 찾은값
                        k-=1
                    while(j<k and nums[j] == nums[j-1]):
                        j+=1
                   
                elif nums[j] + nums[k] > target:
                    k-=1
                else:
                    j+=1

        return output

            
        