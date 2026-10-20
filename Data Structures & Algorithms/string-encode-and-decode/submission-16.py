class Solution:

    def encode(self, strs: List[str]) -> str:
        s = ""
        for words in strs:
            s += str(len(words))+"#"+words
        return s

    def decode(self, s: str) -> List[str]:
        i = 0
        res = []
        while len(s) > i:
            j = i + 1
            while s[j]!= "#":
                j+=1
            length = int(s[i:j]) 
            word = s[j+1:j+1+length]
            res.append(word)
            i = j+1+length 

        return res


















