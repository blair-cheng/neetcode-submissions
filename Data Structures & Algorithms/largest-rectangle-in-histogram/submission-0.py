class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        area = 0
        stack = [] # pair of (index, height)

        for index, height in enumerate(heights):
            start = index 
            while stack and stack[-1][1] > height:
                i, h = stack.pop()
                area = max(area, h * (index - i))
                start = i
            stack.append((start, height))
        
        for index, height in stack:
            area  = max(area, height*(len(heights) - index))
        return area