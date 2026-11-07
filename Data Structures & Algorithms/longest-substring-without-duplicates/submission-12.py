class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        sub = set()
        best = 0
        i = 0

        for char in s:
            while char in sub:
                sub.remove(s[i])
                i += 1
            sub.add(char)
            best = max(best, len(sub))

        return best                

