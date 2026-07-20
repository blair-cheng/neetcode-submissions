class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        dp = [1] * len(nums)
        # dp[i] = length of longest increasing subsequence in nums[:i]
        dp[0] = 1

        for i in range(len(nums)):
            for j in range(i):
                if nums[j]<nums[i]:
                    dp[i] = max(dp[j] + 1,dp[i])

        return max(dp)

