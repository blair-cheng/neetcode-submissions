class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        c = sorted(candidates)
        res = []
        path = []

        def backtrack(i, rem):
            if rem == 0:
                res.append(path.copy())
                return 

            for j in range(i, len(c)):
                if j > i and c[j] == c[j-1]:
                    continue
                if c[j] <= rem:
                    path.append(c[j])
                    backtrack(j+1, rem - c[j])
                    path.pop()


        backtrack(0, target)
        return res
