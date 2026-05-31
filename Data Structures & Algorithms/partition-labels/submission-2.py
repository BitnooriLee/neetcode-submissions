class Solution:
    def partitionLabels(self, s: str) -> List[int]:

        dic = {ch:i for i,ch in enumerate(s)}
        output = []
        end,start = 0,0
        for i,ch in enumerate(s):
            end = max(end, dic[ch])
            if i == end: #start 부터 현재까지 중 그룹의 마지막에 도착했음 
                output.append(end-start+1)
                start = i +1 

        return output
                

        