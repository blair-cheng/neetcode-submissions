class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        adj = {scr: [] for scr, dst in tickets}

        tickets.sort()
        for scr, dst in tickets:
            adj[scr].append(dst)
        res = ["JFK"]
        def dfs(scr):
            if len(res) == len(tickets) + 1:
                return True
            if scr not in adj:
                return False

            temp = list(adj[scr])
            for i, v in enumerate(temp):
                adj[scr].pop(i)
                res.append(v)

                if dfs(v):
                    return True
                adj[scr].insert(i, v)
                res.pop()
            return False
        dfs("JFK")
        return res
            