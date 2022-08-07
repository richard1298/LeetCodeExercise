class Solution:
    def hammingWeight(self, n: int) -> int:
        import math
        if n == 0:
            return 0
        else:
            digits = math.floor(math.log(n,2)) + 1
            i = digits - 1
            result = 0
            temp = n
            while i >= 0:
                bit = temp//(2**i)
                temp = temp - bit*(2**i)
                result += bit
                if temp == 0:
                    break
                i -= 1
            return result