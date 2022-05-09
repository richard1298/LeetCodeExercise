class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        def binsearch_firstneg(nums):
            #this helper function returns the index of the first negative number in a descending array
            #if there is no negative number, return -1
            l , r = 0, len(nums)-1
            result = -1
            if len(nums)==0:
                result = -1
            else:
                if nums[l] <0: 
                    result = 0
                elif nums[r] >0:
                    result = -1
                else: 
                    while l<=r :
                        mid = (l+r)//2
                        if nums[mid] >=0:
                            l = mid +1
                        else:
                            if mid == 0 or nums[mid-1]>=0:
                                result = mid
                                break
                            else:
                                r = mid -1
            return result
        result = 0
        m, n = len(grid), len(grid[0])
        for i in range(m):
            temp = grid[i]
            this_index = binsearch_firstneg(temp)
            if this_index>=0:
                result += n-1-this_index+1
        return result
        