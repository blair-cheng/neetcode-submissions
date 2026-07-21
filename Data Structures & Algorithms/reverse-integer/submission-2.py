class Solution:
    def reverse(self, x: int) -> int:
        Min = -2**31
        Max = 2**31 -1

        sign = 1 if x>=0 else -1
        x = abs(x)
        res = 0
        while x:
            digit = x % 10
            res = res * 10 + digit
            x = x//10

        res = sign * res
        if res > Max or res < Min:
            return 0

        return res