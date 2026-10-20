class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)
        for words in strs:
            count = [0] * 26
            for word in words:
                count[ord(word) - ord("a")] += 1
            res[tuple(count)].append(words)
        return list(res.values())
            



















