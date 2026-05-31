class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        dic = {"1":1, "2":2, "3":3, "4":4, "5":5, "6":6, "7":7, "8":8, "9":9, "0":0}
        if len(num1) < len(num2):
            num1,num2 = num2,num1 
        ans = 0 
        i_num1,i_num2 = 0,0
        for i in range(0,len(num1)):
            i_num1 = 10*i_num1 + dic[num1[i]]

        for i in range(0,len(num2)):
            i_num2 = 10*i_num2 + dic[num2[i]]

        ans = i_num1 * i_num2 

        return str(ans)



        