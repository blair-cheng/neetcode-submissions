class TimeMap:

    def __init__(self):
        self.count = collections.defaultdict(list)
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.count[key].append([timestamp, value])


    def get(self, key: str, timestamp: int) -> str:
        arr = self.count[key]
        i = 0
        j = len(arr)-1
        ans = ""

        while i <= j:
            mid = (i + j)//2
            if arr[mid][0] <= timestamp:
                ans = arr[mid][1]
                i = mid + 1
            else:
                j = mid - 1

        return ans

        
