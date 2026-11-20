class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []
        temp = []


        def backtrack(l):
            if l == len(s):
                res.append(temp.copy())
                return
            
            for r in range(l,len(s)):
                if self.isPa(s,l,r):
                    temp.append(s[l:r+1])
                    backtrack(r + 1)
                    temp.pop()

        backtrack(0)
        return res

    def isPa(self,s,l,r):
        while l<=r:
            if s[l] != s[r]:
                return False
            l += 1
            r -= 1
        return True