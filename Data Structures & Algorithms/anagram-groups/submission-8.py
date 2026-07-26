class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)
        # key: List of corresponding letters, value: str in strs

        for str in strs:
            count = [0] * 26
            for s in str:
                count[ord(s) - ord("a")] += 1
            res[tuple(count)].append(str)
        return list(res.values())