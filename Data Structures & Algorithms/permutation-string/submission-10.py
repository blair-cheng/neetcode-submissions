class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        count1 = collections.defaultdict(int)
        count2 = collections.defaultdict(int)

        for i in range(len(s1)):
            count1[s1[i]] += 1
        n = len(s1)

        i = 0
        for j in range(len(s2)):
            count2[s2[j]] +=1 

            if j - i + 1 == n:
                if count1 == count2:
                    return True
                count2[s2[i]] -= 1

                if count2[s2[i]] == 0:
                    del count2[s2[i]]
                i += 1

        return False
            
            




