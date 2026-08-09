class Solution:
    def minWindow(self, s: str, t: str) -> str:
        window = {} # key=char, val = count of char in s
        tDict = {}

        for c in t:
            tDict[c] = 1 + tDict.get(c, 0)

        l = 0
        res, resLen = [-1,-1], float("inf")
        have, need = 0, len(tDict)

        for r in range(len(s)):
            c = s[r]
            window[c] = 1 + window.get(c, 0)
            if c in tDict and window[c] == tDict[c]:
                have += 1

            while have == need:
                if resLen > (r - l + 1):
                    res = [l, r]
                    resLen = (r - l + 1)
                
                window[s[l]] -= 1
                if s[l] in tDict and window[s[l]] < tDict[s[l]]:
                    have -= 1
                l += 1
        l, r = res
        return s[l:r+1] if resLen != float("inf") else ""








