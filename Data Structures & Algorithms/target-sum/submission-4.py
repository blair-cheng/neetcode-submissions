class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        # dp[(i,current_sum)] = val, i: index of num in mums
        dp = {} # key = (i, current_sum), val = number of different ways in [i:]

        def dfs(i, current_sum):
            if i == len(nums):
                return 1 if current_sum == target else 0

            if (i, current_sum) in dp:
                return dp[(i, current_sum)]

            dp[(i, current_sum)] = dfs(i+1, current_sum + nums[i]) + dfs(i + 1, current_sum - nums[i])
            return dp[(i, current_sum)]
        return dfs(0, 0)