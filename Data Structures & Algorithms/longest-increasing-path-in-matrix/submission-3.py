class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:

        if not matrix and not matrix[0]:
            return 0

        m,n= len(matrix), len(matrix[0])
        curr = [[0]* n for _ in range(m)]
        move = [(0,1),(1,0),(-1,0),(0,-1)]
        ans = 0


        def dfs(i,j):
            if curr[i][j] != 0:
                return curr[i][j]
            best = 1 # 자기자신 길이 
            for di, dj in move:
                if 0<= i+di <m and 0<=j+dj<n and matrix[i][j]> matrix[i+di][j+dj]:
                    best = max(best, 1+ dfs(i+di,j+dj)) #옆에서 자기자신으로 들어온다고 생각
                
            curr[i][j]= best
            return best

        for i in range(m):
            for j in range(n):
                dfs(i,j)

        for i in range(m):
            for j in range(n):
                ans = max(ans, curr[i][j])

        return ans
                        

        