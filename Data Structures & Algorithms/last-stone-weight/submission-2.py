class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        hq = []
        for stone in stones:
            heapq.heappush(hq,-1*stone)

        while len(hq)>1:
            max1 = heapq.heappop(hq)
            max2 = heapq.heappop(hq)
            rem = abs(max1 - max2)
            if rem > 0:
                heapq.heappush(hq,-1*rem)  
        return 0 if not hq else -1 * hq[0]  


