class Solution:
    def findTheDistanceValue(self, arr1: List[int], arr2: List[int], d: int) -> int:
        def binsearch(nums,target):
            #this function finds the index of the last element that is smaller than or equal to the target value
            #nums[output] <= target
            l, r = 0, len(nums)-1
            result = -1
            while l <= r:
                mid = (l+r)//2
                if nums[mid]>target:
                    r = mid -1
                elif nums[mid]<= target:
                    if mid == len(nums) - 1:
                        result = mid
                        break
                    else:
                        if nums[mid+1]> target:
                            result = mid
                            break
                        else:
                            l = mid+1
            return result
        arr2 = list(set(arr2))
        arr2.sort()
        result = 0
        for i, elem in enumerate(arr1):
            temp_index = binsearch(arr2,elem)
            #print('temp_index=',temp_index)
            if temp_index == -1:
                if arr2[0]-d>elem:
                    result += 1
            elif temp_index == len(arr2)-1:
                if arr2[-1]+d < elem:
                    result += 1
            else:
                include = (arr2[temp_index]+d <elem) and (arr2[temp_index+1]-d>elem)
                if include:
                    result += 1
        return result 