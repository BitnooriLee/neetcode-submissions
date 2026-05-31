class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        if num1 == "0" or num2=="0":
            return '0'
        m,n = len(num1), len(num2)
        res = [0]*(m+n)
        for i in range(m-1,-1,-1):
            for j in range(n-1,-1,-1):
                p1 = i+j
                p2 = i+j+1 # j가 하나 더 내려가면서 p2가 p1이ㅣ 됨 
                mul = (ord(num1[i])-ord('0'))*(ord(num2[j])-ord('0'))
                total = mul + res[p2]
                res[p1] += total//10
                res[p2] = total%10
        return "".join(map(str,res)).lstrip('0')
        

#"".join(res) 이게 되려면 ["1","2","3"] 이런식
# "".join(map(str,res) 이건 [1,2,3] -> "123" 
