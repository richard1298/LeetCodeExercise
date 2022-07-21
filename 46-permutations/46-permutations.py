class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        
        def backtracking(nums):
            result = []
            if len(nums) == 1:
                return [nums[:]]
            for i in range(len(nums)):
                n = nums.pop(0)
                perm = backtracking(nums)
                
                for k in perm:
                    k.append(n)
                result.extend(perm)
                nums.append(n)
            return result
        
        return backtracking(nums)
                