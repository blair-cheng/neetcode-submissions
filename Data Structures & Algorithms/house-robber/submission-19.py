class Solution:
    def rob(self, nums: List[int]) -> int:
        # let dp[i] be the total money from rob house i to house n-1 
        n = len(nums)
        dp = [0 for i in range(n+2)]
        dp[n-1] = nums[n-1]

        for i in range(n-1, -1,-1):
            dp[i] = max(nums[i] + dp[i+2], dp[i+1])
        return dp[0]