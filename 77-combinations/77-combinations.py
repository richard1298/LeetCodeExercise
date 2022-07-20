class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        result = []

        def backtracking(n, k, idx, path):
            if len(path) == k:
                result.append(path)
            else:
                i = 0
                while i + idx <= n:
                    backtracking(n,k,i+idx+1, path + [i + idx])
                    i += 1


        backtracking(n,k,1,[])
        return result