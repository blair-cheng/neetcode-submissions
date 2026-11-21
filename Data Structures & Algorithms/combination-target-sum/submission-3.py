class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        path = []

        def backtrack(start, rem):
            if rem == 0:
                res.append(path.copy())
                return 

            for i in range(start,len(nums)):
                if rem - nums[i] >=0:
                    path.append(nums[i])
                    backtrack(i, rem - nums[i])
                    path.pop()


        backtrack(0,target)
        return res