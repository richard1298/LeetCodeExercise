class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        i = 0
        while i <= len(nums) - 1:
            #print('i=',i)
            if nums[i]%2==0:
                i +=1
            else:
                j = i+1
                while j <=len(nums)-1:
                    #print('j=',j)
                    if nums[j]%2 ==0:
                        nums[i],nums[j] = nums[j],nums[i]
                        break
                    j+=1
                i+=1
        return nums       