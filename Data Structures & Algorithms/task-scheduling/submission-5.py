class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        count = collections.defaultdict(int)
        for task in tasks:
            count[task] += 1  
        time = 0
        q = collections.deque()
        max_heap = []

        for key, value in count.items():
            heapq.heappush(max_heap, (-value, task))

        while max_heap or q:
            if q and q[0][2] <= time:
                task, value, ready_time = q.popleft()
                heapq.heappush(max_heap,(value, task))
            if max_heap:
                value, task = heapq.heappop(max_heap)
                value += 1
                if value != 0:
                    q.append((task,value,time + n + 1))

            
            time += 1



        return time



        































        count = Counter(tasks)
        maxHeap = [-cnt for cnt in count.values()]

        q = deque()
        time = 0
        heapq.heapify(maxHeap)

        while maxHeap or q:
            time += 1
            if maxHeap:
                cnt = 1 + heapq.heappop(maxHeap)
                if cnt:
                    q.append([cnt, time + n])
            if q and q[0][1] == time:
                heapq.heappush(maxHeap, q.popleft()[0])
        return time