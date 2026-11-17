class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        res = [0]*len(temperatures)

        for index, tem in enumerate(temperatures):
            while stack and tem > stack[-1][0]:
                t, i = stack.pop()
                res[i] = index - i
            stack.append((tem, index))
        return res
