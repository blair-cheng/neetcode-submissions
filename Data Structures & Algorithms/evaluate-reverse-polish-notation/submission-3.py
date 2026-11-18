class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for token in tokens:
            if token not in "+-*/":
                stack.append(int(token))
            else:
                right = stack.pop()
                left = stack.pop()
                if token == "+":
                    res = right + left
                elif token == "-":
                    res = left - right
                elif token == "*":
                    res = right * left
                else:
                    res = int(left/right)
                stack.append(res)
        return stack[-1]
            