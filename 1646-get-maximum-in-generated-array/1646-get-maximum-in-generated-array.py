class Solution:
    def getMaximumGenerated(self, n: int) -> int:
        result = [0,1]
        i = 2
        while i <= n:
            if i%2 ==0:
                result.append(result[i//2])
            else:
                result.append(result[(i+1)//2]+result[(i-1)//2])
            i+=1
        if n <=1:
            return result[n]
        else:
            return max(result)