class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        result = []
        tmpsum = 0
        i=0
        while i <= len(nums) - 1:
            tmpsum += nums[i]
            result.append(tmpsum)
            i+=1
        return result