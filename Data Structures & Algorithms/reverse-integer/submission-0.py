class Solution:
    def reverse(self, x: int) -> int:
        Min = -2**31
        Max = 2**31 -1

        res = 0
        while x:
            digit = int(math.fmod(x,10))
            x = int(x/10)

            if (res > Max//10 or 
                (res == Max // 10 and digit >= Max%10)):
                return 0
            if (res < Min//10 or 
                (res == Min//10 and digit <= Min%10)):
                return 0
            res = (res * 10) + digit
        return res