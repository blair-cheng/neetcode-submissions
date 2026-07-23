class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        if "0" in [num1,num2]: 
            return "0"

        res = [0] * (len(num1) + len(num2))
        for i in range(len(num1)-1,-1,-1):
            for j in range(len(num2)-1,-1,-1):
                digit1 = ord(num1[i]) - ord("0")
                digit2 = ord(num2[j]) - ord("0")
                mul = digit1 * digit2

                low = i + j + 1
                high = i + j 
                total = mul + res[low]
                res[low] = total % 10
                res[high] += total // 10

        start = 0
        while start < len(res) and res[start] ==0:
            start += 1
        return "".join(map(str,res[start::]))
        
        