class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        n = len(tickets)
        tickets.sort()
        dic = { s : [] for s,d in tickets}
        for s,d in tickets:
            dic[s].append(d)
        route = []
        
        
        def dfs(u):
            while(u in dic and dic[u]):
                v = heapq.heappop(dic[u])
                dfs(v)
            route.append(u)
        dfs("JFK")
        return route[::-1]

                


        

        