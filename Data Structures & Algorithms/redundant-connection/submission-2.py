class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges)
        parent = list(range(n+1))


        def find(x):

            while parent[x]!= x:
                x = parent[x]
            return x

        def union(a,b):
            if find(a) == find(b):
                return True
            else:
                parent[find(a)] = find(b)
                return False

        for a,b in edges:
            if union(a,b):
                return [a,b]  



