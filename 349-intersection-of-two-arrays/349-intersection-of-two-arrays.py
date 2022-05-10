class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        a = list(set(nums1))
        nums2.sort()
        result = []
        def binsearch(nums,target):
            l, r = 0,len(nums)-1
            result = -1
            while l<=r:
                mid = (l+r)//2
                if nums[mid]>target:
                    r = mid - 1
                elif nums[mid]<target:
                    l = mid + 1
                else:
                    result = mid
                    r = mid - 1 
            if result <0:
                return False
            else:
                return True 
        for i in range(len(a)):
            if binsearch(nums2,a[i]):
                result.append(a[i])
        return result