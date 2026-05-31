class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        tickets.sort()
        itr = defaultdict(list)
        for s,d in tickets:
            itr[s].append(d)

        res = ["JFK"]

        def dfs(src):
            if len(res) == len(tickets) + 1:
                return True
            if src not in itr:
                return False

            tmp = list(itr[src])
            for i,v in enumerate(tmp):
                itr[src].pop(i)
                res.append(v)
                if dfs(v):
                    return True
                itr[src].insert(i,v)
                res.pop()
            return False

        dfs("JFK")

        return res 