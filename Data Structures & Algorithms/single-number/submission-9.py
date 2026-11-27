class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        #XOR
        xor = 0
        for num in nums:
            xor^= num

        return xor 

    # nums[1:] 파이선 슬라이싱은 새로운 리스트가 생김.. a^a = 0, a^0=a 활용 