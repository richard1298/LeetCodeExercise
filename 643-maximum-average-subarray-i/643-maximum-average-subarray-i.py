class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        s = sum(nums[0:k])
        result = s
        i = 1
        while i+k-1<=len(nums)-1:
            s = s-nums[i-1]+nums[i+k-1]
            result = max(result,s)
            i+=1
        return result/k