class Solution:
    def maxSubsequence(self, nums: List[int], k: int) -> List[int]:
        import heapq
        nums_t = [-elem for elem in nums]
        heapq.heapify(nums_t)
        i = 1
        l = []
        while i<=k:
            temp = -heapq.heappop(nums_t)
            l.append(temp)
            i+=1
        result = []
        for j in nums:
            if j in l:
                result.append(j)
                l.remove(j)
        return result
            
        