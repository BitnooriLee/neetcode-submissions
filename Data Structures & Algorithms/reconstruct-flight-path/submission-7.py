class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        tickets.sort()
        adj = defaultdict(list)

        res = ["JFK"]
        for s,d in tickets:
            adj[s].append(d)

        
        def dfs(src): # T/F and update res 
            if len(res) == len(tickets)+1:
                return True

            if src not in adj:
                return False
            
            tmp = list(adj[src]) # 순서중요 

            for i,v in enumerate(tmp):
                adj[src].pop(i)
                res.append(v)
                if dfs(v): return True
                adj[src].insert(i,v)
                res.pop()
            return False    



        
            

        dfs("JFK")
        
        return res 