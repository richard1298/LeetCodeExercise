class Solution:
    def reverseBits(self, n: int) -> int:
        result = []
        i = 32
        temp = n
        while i >= 1:
            bits = temp//2**(i-1)
            temp = temp - bits * 2**(i-1)
            result.append(str(bits))
            i -= 1
        result.reverse()
        a = ''.join(result)
        return int(a,2)
        