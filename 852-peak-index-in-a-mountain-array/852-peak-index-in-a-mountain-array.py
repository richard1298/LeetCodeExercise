class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        l, r = 0, len(arr)-1
        result = -1
        while l<=r:
            mid = (l+r)//2
            if arr[mid-1]<arr[mid] and arr[mid]<arr[mid+1]:
                l = mid +1
            elif arr[mid-1]>arr[mid] and arr[mid]>arr[mid+1]:
                r = mid
            else:
                result = mid
                break
        return result 
        