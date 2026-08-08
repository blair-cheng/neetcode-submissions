class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left = 1
        right = max(piles)

        while left <= right: 
            time = 0
            mid = (left + right) // 2

            for p in piles:
                time += (p + mid -1) // mid
            if time <= h:
                res = mid
                right = mid - 1
            else: 
                left = mid + 1
        return res
            
                



