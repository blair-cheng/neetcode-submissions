class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        res = []
        visit = {}
        adj = {w:set() for word in words for w in word}

        for i in range(len(words)-1):
            word1, word2 = words[i], words[i+1]
            minLen = min(len(word1), len(word2))
            
            if len(word1)>len(word2) and word1[:minLen] == word2[:minLen]:
                return ""
            
            for j in range(minLen):
                if word1[j] != word2[j]:
                    adj[word1[j]].add(word2[j])
                    break

        def dfs(w):
            if w in visit:
                return visit[w]
            visit[w] = True
            for nei in adj[w]:
                if dfs(nei):
                    return True
            visit[w] = False
            res.append(w)
        for w in adj:
            if dfs(w):
                return ""

        return  "".join(res[::-1])