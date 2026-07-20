class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        target = sum(nums) / 2
        nums:sort()
        if sum(nums) % 2 or nums[-1] > target:
            return False 

        dp = set()
        dp.add(0)

        for i in range(len(nums) -1, -1, -1):
            nextDP = set()
            for t in dp:
                nextDP.add(t + nums[i])
                nextDP.add(t)
            dp = nextDP
        return True if target in dp else False

