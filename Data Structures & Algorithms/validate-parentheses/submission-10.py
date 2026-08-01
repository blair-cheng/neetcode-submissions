class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        rightLeft = {")":"(", "]":"[", "}":"{"}

        for c in s:
            # if right 
            if c in rightLeft:
                if stack and stack[-1] == rightLeft[c]  :
                    stack.pop()
                else: 
                    return False
                
            # if left 
            else: 
                stack.append(c)

        return True if not stack else False