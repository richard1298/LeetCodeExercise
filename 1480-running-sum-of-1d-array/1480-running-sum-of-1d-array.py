class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        result = []
        for i in range(len(nums)):
            result.append(sum(nums[0:i+1]))
        return result