class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        anaDict = defaultdict(int)
        if len(s) != len(t):
            return False
        
        for c in s:
            anaDict[c] += 1
        for c in t:
            anaDict[c] -= 1
            if anaDict[c] <0:
                return False

        return True

