class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        iter = defaultdict(list)
        tickets.sort()

        for s,d in tickets:
            iter[s].append(d)
        res = ["JFK"]

        
        def dfs(src):
            if len(res) == len(tickets)+1:
                return True
            
            if src not in iter:
                return False

            tmp = list(iter[src])
            for i,v in enumerate(tmp):
                iter[src].pop(i)
                res.append(v)
                if dfs(v):
                    return True
                iter[src].insert(i,v)
                res.pop()
            return False

        dfs("JFK")
        return res 

        


        