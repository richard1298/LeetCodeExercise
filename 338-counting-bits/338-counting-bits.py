class Solution:
    def countBits(self, n: int) -> List[int]:
        result = [0]
        for i in list(range(1,n+1)):
            if i % 2 ==1:
                result.append(result[i-1]+1)
            else:
                result.append(result[i//2])
        return result