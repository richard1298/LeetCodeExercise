class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        self.result = []
        def generate_helper(n):
            if n == 1:
                self.result.append([1])
            elif n ==2:
                self.result.append([1])
                self.result.append([1,1])
            else:
                generate_helper(n-1)
                temp = self.result[-1]
                new = [1] + [temp[i]+temp[i+1] for i in range(len(temp)-1)] + [1]
                self.result.append(new)
        generate_helper(numRows)
        return self.result
                
                