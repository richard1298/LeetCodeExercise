class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        result = []
        i = 0
        j = 1
        k = len(nums)-1
        while i <=len(nums)-3:
            target = -nums[i]
            j = i+1
            k = len(nums) - 1
            while j <k:
                if nums[j] + nums[k] == target:
                    if [nums[i],nums[j],nums[k]] not in result:
                        result.append([nums[i],nums[j],nums[k]])
                    j += 1
                elif nums[j] + nums[k] < target:
                    j += 1
                else:
                    k -= 1
            i += 1
        return result
        