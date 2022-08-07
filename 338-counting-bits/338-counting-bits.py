class Solution:
    def countBits(self, n: int) -> List[int]:
        i = 0
        result = []
        while i <= n:
            if i == 0:
                result.append(0)
            else:
                if i%2 == 0:
                    result.append(result[i//2])
                else:
                    result.append(result[i-1]+1)
            i+= 1
        return result
                
            