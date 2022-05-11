class Solution:
    def fairCandySwap(self, aliceSizes: List[int], bobSizes: List[int]) -> List[int]:
        def binsearch(nums,target):
        #returns the index of target; -1 if not found
            l, r = 0, len(nums)-1
            result = -1
            while l<=r:
                mid = (l+r)//2
                if nums[mid] > target:
                    r = mid - 1
                elif nums[mid] < target:
                    l = mid + 1
                else:
                    result = mid
                    r = mid - 1
            return result
        total = sum(aliceSizes) + sum(bobSizes)
        k = 0.5*total-sum(aliceSizes)
        bobSizes.sort()
        result = []
        i = 0
        while i < len(aliceSizes):
            idx = binsearch(bobSizes,aliceSizes[i]+k)
            if idx != -1:
                result = [aliceSizes[i], bobSizes[idx]]
                break
            else:
                i+=1
        return result