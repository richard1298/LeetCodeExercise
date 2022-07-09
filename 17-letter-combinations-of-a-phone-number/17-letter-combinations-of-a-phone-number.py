class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        self.dic = {'2':'abc','3':'def','4':'ghi','5':'jkl',
                      '6':'mno','7':'pqrs','8':'tuv','9':'wxyz'}
        
        def com_helper(digits):
            if len(digits)> 1:
                l = digits[0]
                tel = self.dic[l]
                prev = com_helper(digits[1::])
                result = []
                for i in range(len(tel)):
                    result = result + [tel[i] + elem for elem in prev]
                return result
            else:
                if len(digits) == 1:
                    return list(self.dic[digits])
                else:
                    return []
        return com_helper(digits)
