class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        result = []
        def backtracking(openP, closeP, path):
            if openP == closeP == n:
                result.append(path)
            if openP < n:
                backtracking(openP+1,closeP,path+'(')
            if closeP < openP:
                backtracking(openP, closeP+1,path+')')
        backtracking(0,0,'')
        
        return result
                
                
                