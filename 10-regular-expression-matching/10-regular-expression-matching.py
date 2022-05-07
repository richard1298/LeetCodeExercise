class Solution:
    def isMatch(self, s: str, p: str) -> bool:
            #this is the parent function call that matches the string characteristics
        cache = {}
        def dfs(i, j):
            #print("pair:(",i,",",j,")")
            if (i,j) in cache:
                return cache[(i,j)]
            #i,j is the index that's pointing to the position of the string/pattern
            if i >= len(s) and j >= len(p):
                #this means all strings are matched with all patterns
                return True
            if j >= len(p):
                #this means there are unmatched strings; pattern string is exhausted 
                return False
            match = i<len(s) and (s[i] == p [j] or p[j] == '.')
            if j+1 < len(p) and p[j+1] == '*':
                cache[(i,j)] = (match and dfs(i+1,j)) or dfs(i,j+2)
                #print("need to check pair:(",i+1,",",j,")")
                #print("need to check pair:(",i,",",j+2,")")
                #sample test case: input string s='aaabaaa', pattern p='a*b*a*'
                return cache[(i,j)]
            if match:
                cache[(i,j)] = dfs(i+1,j+1)
                return dfs(i+1,j+1)
            return False
        return dfs(0,0)