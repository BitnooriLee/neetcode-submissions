class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        itr = defaultdict(list)
        tickets.sort()
        for u,v in tickets:
            itr[u].append(v)
        
        res = ["JFK"]

        def dfs(src):
            if len(res) == len(tickets)+1:
                return True
            
            if src not in itr:
                return False

            tmp = list(itr[src]) #back tracking 하려고 
            for i,v in enumerate(tmp):
                itr[src].pop(i)
                res.append(v)
                if dfs(v): return True
                itr[src].insert(i,v)
                res.pop()
            return False
        dfs("JFK")
        return res
