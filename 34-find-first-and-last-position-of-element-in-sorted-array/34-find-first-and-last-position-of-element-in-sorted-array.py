class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def binsearch_first(nums,target):
            result = -1
            l, r = 0, len(nums) - 1
            while l <= r:
                mid = (l+r) // 2
                if nums[mid] == target:
                    if mid == 0:
                        result = 0
                        break
                    else:
                        if nums[mid-1]==target:
                            r = mid - 1
                        else:
                            result = mid
                            break
                elif nums[mid] > target:
                    r = mid - 1
                else:
                    l = mid + 1
            return result
        def binsearch_last(nums,target):
            result = -1
            l, r = 0, len(nums) - 1
            while l <= r:
                mid = (l+r) // 2
                if nums[mid] == target:
                    if mid == len(nums) - 1:
                        result = mid
                        break
                    else:
                        if nums[mid+1]==target:
                            l = mid + 1
                        else:
                            result = mid
                            break
                elif nums[mid] > target:
                    r = mid - 1
                else:
                    l = mid + 1
            return result
        
        firstidx = binsearch_first(nums,target)
        if firstidx == -1:
            return [-1,-1]
        else:
            lastidx = binsearch_last(nums,target)
            return [firstidx,lastidx]
            