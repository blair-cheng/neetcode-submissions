class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # a + b + c = 0
        # a + b = -1 * c 
        nums.sort()
        res = []

        for i, c in enumerate(nums):
            if i > 0 and c == nums[i - 1]:
                continue

            l, r = i+1, len(nums)-1
            while l < r:
                threeSum = c + nums[l] + nums[r]
                if threeSum > 0:
                    r -= 1
                elif threeSum < 0: 
                    l += 1
                else:
                    res.append([nums[l], nums[r], c])
                    l += 1
                    while nums[l] == nums[l-1] and l < r:
                        l += 1
        return res







