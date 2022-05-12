class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        nums.sort()
        nums.reverse()
        #print(nums)
        result = nums[0]-nums[k-1]
        i = 0
        while i+k-1<=len(nums)-1:
            result = min(result,nums[i]-nums[i+k-1])
            i +=1
        return result

        