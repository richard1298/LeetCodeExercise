class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        def binsearch(nums):
            #this function returns the index of the first non-negative element
            #returns -1 if all elements are negative
            l, r = 0, len(nums)-1
            result = -1
            while l<=r:
                #print('start l =',l,"start r =",r)
                mid = (l+r)//2
                if nums[mid]<0:
                    l=mid+1
                elif nums[mid]>=0:
                    if mid == 0:
                        result = 0
                        break
                    elif nums[mid-1]>=0:
                        r = mid-1
                    else:
                        #print('hit!!')
                        result = mid
                        break
                #print('updated l =',l,"updated r =",r)
            return result    
        idx = binsearch(nums)
        result = []
        if idx == -1:
            result = [nums[-i-1]**2 for i in range(len(nums))]
        else:
            l = idx - 1
            r = idx
            while l>=0 and r <=len(nums)-1:
                #print('l=', l,'right=',r)
                if abs(nums[l])>=nums[r]:
                    result.append(nums[r]**2)
                    r+=1
                else:
                    result.append(nums[l]**2)
                    l-=1
            while r<=len(nums)-1:
                #print('right=',r)
                result.append(nums[r]**2)
                r+=1
            while l >=0:
                #print('left=',l)
                result.append(nums[l]**2)
                l-=1
        return result