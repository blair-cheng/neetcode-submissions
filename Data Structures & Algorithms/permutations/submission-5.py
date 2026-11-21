class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        path = []
        res = []

        def backtrack():
            if len(path) == len(nums):
                res.append(path.copy())
                return 
            for j in range(len(nums)):
                if nums[j] in path:
                    continue
                path.append(nums[j])
                backtrack()
                path.pop()
        backtrack()
        return res