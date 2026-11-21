class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        n =  len(digits) 
        res = []
        path = []
        digitMap = {2:"abc", 3:"def", 4:"ghi", 5:"jkl", 6:"mno", 7:"pqrs", 8:"tuv", 9:"wxyz"}

        def backtrack(i):

            if i == n ==len(path):
                res.append("".join(path))
                return 

            for j in range(i,n):
                letters = digitMap[int(digits[j])]
                for l in letters:
                    path.append(l)
                    backtrack(j+1)
                    path.pop()
        backtrack(0)
        return [] if n == 0 else res