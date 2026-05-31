class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        path = []

        def backtrack(i):
            if i == len(nums):
                res.append(path.copy())
                return

            path.append(nums[i])
            backtrack(i+1)
            path.pop()
            backtrack(i+1)

        backtrack(0)

        return res

    #Big O -> time( 2^n)
    #Space -> 재귀스택 n, res 에 결과쓰기 n*2^n