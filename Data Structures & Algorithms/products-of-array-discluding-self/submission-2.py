class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # left: list of n + 2 numbers, index [:1] to [:n+3]
        # right: [n-]
        n = len(nums)
        res = [1] * n
        
        prefix = 1
        for i in range(n):
            res[i] = prefix
            prefix *= nums[i]

        postfix = 1
        for i in range(n-1,-1,-1):
            res[i]*= postfix
            postfix *= nums[i]

        return res
