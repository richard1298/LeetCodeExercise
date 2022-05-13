class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        result = False
        i = 0
        rep={}
        if k ==0:
            return result
        if len(nums)<=k:
            if len(nums)!=len(set(nums)):
                return True
            return result
        else:
            first = nums[0:k+1]
            if len(first) != len(set(first)):
                return True
            else:
                for i in range(k):
                    rep[nums[i]]=i
                j = 0
                while k+j<=len(nums)-1:
                    if nums[k+j] in rep:
                        result = True
                        break
                    else:
                        del rep[nums[j]]
                        rep[nums[k+j]] = k+j
                        j+=1
                return result
