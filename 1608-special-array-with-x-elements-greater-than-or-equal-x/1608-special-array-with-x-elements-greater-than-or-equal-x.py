class Solution:
    def specialArray(self, nums: List[int]) -> int:
        def binsearch(nums,target):
        #this function finds the index of the first element that is smaller than target
        #nums[output] < target
        #if all elements are smaller than target, returns len(nums-1)
        #if all elements are larger than target, returns -1
            l, r = 0, len(nums)-1
            result = -1
            while l <= r:  
                mid = (l+r)//2
                #print('l=',l,'r=',r)
                #print('mid=',mid)
                if nums[mid]>=target:
                    r = mid - 1
                else:
                    if mid == len(nums) - 1:
                        result = mid
                        break
                    else:
                        if nums[mid+1]>=target:
                            result = mid
                            break
                        else:
                            l = mid +1
            return result
        nums.sort()
        i = 0
        result = -1
        while i <= len(nums):
            temp_index = binsearch(nums,i)
            num_elem = len(nums)-temp_index-1
            if num_elem == i:
                result = i
                break
            else:
                i+=1
        return result
        