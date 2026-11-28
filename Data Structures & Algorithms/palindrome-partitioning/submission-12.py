class Solution:
    def partition(self, s: str) -> List[List[str]]:
        output = []
        #isPal? 
        def isPal(cur):
            i,j = 0, len(cur)-1
            while(i<j):
                if cur[i]!=cur[j]:
                    return False
                i+=1
                j-=1
            return True

        def bt(i,tmp):
            if i == len(s):
                output.append(tmp[:])
                return 
            #i에서 j까지가 Pal인지 판단 
            for j in range(i,len(s)):
                piece = s[i:j+1]
                if isPal(piece):
                    tmp.append("".join(piece))
                    bt(j+1, tmp) #어디서부터 시작인지 
                    tmp.pop()

        bt(0,[])


        return output

        