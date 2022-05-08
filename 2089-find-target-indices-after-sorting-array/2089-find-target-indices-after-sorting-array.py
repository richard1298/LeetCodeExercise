class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        nums.sort()
        l = 0
        r = len(nums)-1
        result = []
        while l<= r:
            mid = (l+r)//2
            if target == nums[mid]:
                result = mid
                r = mid - 1
            # if the target is less than the middle element, discard the right half
            elif target < nums[mid]:
                r = mid - 1
            # if the target is more than the middle element, discard the left half
            else:
                l = mid + 1
        #print(result)
        if result == []:
            return result
        else:
            temp = result + 1
            result = [result]
            while temp <len(nums) and nums[temp] == target:
                result.append(temp)
                temp+=1
            return result
            
        