class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        i, j = 1, max(piles)


        while i <= j:
            totle = 0
            mid = (i + j) // 2
            for pile in piles:
                if pile % mid == 0:
                    totle += pile // mid
                else:
                    totle += pile//mid + 1
            if totle <= h:
                best = mid
                j = mid - 1
            else:
                i = mid + 1

        return best
            
        