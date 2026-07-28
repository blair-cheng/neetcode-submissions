class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        string_set = set()
        l = 0
        res = 0 

        for r in range(len(s)):
            while s[r] in string_set:
                string_set.remove(s[l])
                l += 1
            string_set.add(s[r])
            res = max(res, r - l + 1)
        return res




