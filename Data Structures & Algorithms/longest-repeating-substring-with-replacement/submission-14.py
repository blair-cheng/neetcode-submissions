class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        res = 0
        l = 0
        count = defaultdict(int) # key: str , val: count

        for r in range(len(s)):
            count[s[r]] += 1  
            while (r - l + 1) - max(count.values()) > k:
                count[s[l]] -= 1
                l += 1
            res = max(res, r - l + 1)
        return res
            

