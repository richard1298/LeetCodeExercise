class Solution:
    def search(self, nums: List[int], target: int) -> int:
        def find_peak(nums):
            l, r = 0, len(nums) - 1
            result = -1
            while l <= r:
                mid = (l + r)//2
                if mid<len(nums)-1:
                    if nums[mid]>nums[mid+1]:
                        result = mid
                        break
                    else:
                        if nums[mid]<nums[0]:
                            r = mid-1
                        else:
                            l = mid + 1
                elif mid == len(nums) - 1:
                    r -= 1
            return result
        idx = find_peak(nums)
        if idx == -1:
            l, r = 0, len(nums) -1
        else:
            if target >= nums[0]:
                l, r = 0, idx
            else:
                l, r = idx+1, len(nums) - 1
        result = -1
        while l <= r:
            mid = (l+r)//2
            if nums[mid]==target:
                result = mid
                break
            elif nums[mid] > target:
                r = mid-1
            else:
                l = mid+1
        return result