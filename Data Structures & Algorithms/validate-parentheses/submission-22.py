class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        match = {")": "(", "]": "[", "}": "{"}

        for b in s:

            if b in match:
                if stack and stack[-1] == match[b]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(b)
        return not stack