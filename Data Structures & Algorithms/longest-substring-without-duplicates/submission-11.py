class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        sub = set()
        best = 0
        i, j = 0, 0

        for char in s:
            while char in sub:
                sub.remove(s[i])
                i += 1
            sub.add(char)
            j += 1
            best = max(best, len(sub))

        return best                

