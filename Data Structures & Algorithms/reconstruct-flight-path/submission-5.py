class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        res = []
        adj = collections.defaultdict(list)

        for src, des in sorted(tickets, reverse = True):
            adj[src].append(des)
        
        def dfs(src):
            while adj[src]:
                dst = adj[src].pop()
                dfs(dst)
            res.append(src)
            

        dfs("JFK")
        return res[::-1]



