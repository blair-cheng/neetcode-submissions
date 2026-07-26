class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # output [0, 1]
        minusMap = {} # minusMap[(target-i)] =val/i

        for i,num in enumerate(nums):
            diff = target - num
            if diff in minusMap:
                return [minusMap[diff],i]
            minusMap[num] = i

