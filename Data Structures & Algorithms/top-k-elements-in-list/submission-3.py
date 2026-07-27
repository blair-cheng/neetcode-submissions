class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # output list[3,4]
        # dict[num:frequency]
        # heap[[-frequency, num],...]
        dict = defaultdict(int)
        maxHeap = []
        res = []

        for num in nums:
            dict[(num)] += 1
        
        for num, freq in dict.items():
            heapq.heappush(maxHeap,[-freq,num])

        for _ in range(k):
            freq,num = heapq.heappop(maxHeap)
            res.append(num)

        return res

