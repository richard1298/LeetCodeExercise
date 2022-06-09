class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        def getRow_helper(n):
            if n==0:
                return [1]
            elif n==1:
                return [1,1]
            else:
                i = 0 
                temp = getRow_helper(n-1)
                result = [1] + [temp[i]+temp[i+1] for i in range(0,len(temp)-1)] + [1]
                return result
        return getRow_helper(rowIndex)
                