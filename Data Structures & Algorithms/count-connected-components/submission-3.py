class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        res = n
        parent = list(range(n))

        def find(x):
            while parent[x] != x:
                x = parent[x]
            return x

        for a,b in edges:
            if find(a)!=find(b):
                parent[find(a)] = find(b)
                res -= 1
        return res



        