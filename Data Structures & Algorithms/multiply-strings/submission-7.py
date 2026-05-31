class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        if num1 == "0" or num2 =="0":
            return "0"
        m,n = len(num1), len(num2)
        res = [0]*(m+n)

        for i in range(m-1,-1,-1):
            for j in range(n-1,-1,-1):
                a = ord(num1[i]) - ord('0')
                b = ord(num2[j]) - ord('0')

                p2 = i + j + 1
                p1 = i + j
                total = a*b + res[p2]
                
                res[p2] = total%10
                res[p1] += total//10 #한자리 더 위 올라갈수록 숫자 작아짐 캐리는 누적


        #reading 0 제거 

        k = 0 
        for n in res:
            if n == 0:
                k+= 1 
            else:
                break

        return "".join(map(str, res[k:]))