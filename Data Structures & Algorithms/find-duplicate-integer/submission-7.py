class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        
        #사이클 내에서 만나기? 
        slow = fast = 0
        while(True):
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break
        # 2단계 입구찾기 
        slow2 = 0 
        while(slow!= slow2):
            slow = nums[slow]
            slow2 = nums[slow2]
        
        return slow