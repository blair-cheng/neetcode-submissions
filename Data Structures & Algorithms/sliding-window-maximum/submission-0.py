class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        output = []
        q = collections.deque() # index

        for r in range(len(nums)):
            # 1. maintain monotonic decreasing order
            while q and nums[q[-1]] <= nums[r]:
                q.pop()
            # 2. add the current element's index to the back of the deque
            q.append(r)

            # 3 evict expired element from the front 
            if (r - k + 1) > q[0]:
                q.popleft()
            # 4. append to result
            if (r + 1) >= k:
                output.append(nums[q[0]])
            
        return output



