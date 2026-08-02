class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0]*len(temperatures) # curr index - stack[-1][0]
        stack = [] # monotonic stack [ [t, i], ]

        for index, num in enumerate(temperatures):
            while stack and stack[-1][1] < num:
                si, _ =  stack.pop()
                res[si] = (index - si)
            stack.append([index, num])
        return res 
        
