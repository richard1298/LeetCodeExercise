class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:       
        m, n = len(mat), len(mat[0])
        def binsearch(nums,target):
            #this helper function returns the first occurrence of target in nums
            l, r = 0, len(nums)-1
            result = len(nums) 
            while l<=r:
                mid = (l+r)//2
                if nums[mid]>target:
                    l = mid+1
                elif nums[mid]<target:
                    r = mid-1
                else:
                    result = mid
                    r = mid-1
            return result
        s = []

        for i in range(m):
            temp = mat[i]
            num_sol = binsearch(temp,0)
            s.append([i,num_sol])
        #print(s)
        #this is an important method to sort a 2-d list 
        s.sort(key = lambda x:x[1])
        result = []
        for j in range(k):
            result.append(s[j][0])
        return result
        
        