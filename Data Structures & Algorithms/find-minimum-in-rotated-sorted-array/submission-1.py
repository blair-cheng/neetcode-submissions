class Solution:
    def findMin(self, nums: List[int]) -> int:
        minn = 1001

        l, r = 0, len(nums)-1

        while l <= r:
            mid = (l + r) //2 
            if nums[mid]<= nums[r]:
                minn = min(minn, nums[mid])
                r = mid - 1
            elif nums[l] <= nums[mid]:
                minn = min(minn, nums[l])
                l = mid + 1
        return minn