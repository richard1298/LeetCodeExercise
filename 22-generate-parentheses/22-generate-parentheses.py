class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        result = []
        def par_helper(openP,closeP,path):
            if openP == closeP == n:
                result.append(path)
                return
            if openP<n:
                par_helper(openP + 1, closeP, path + '(')
            if closeP < openP:
                par_helper(openP, closeP + 1, path + ')')
        par_helper(0,0,'')
        return result