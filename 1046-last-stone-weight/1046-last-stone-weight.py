class Solution:
    import heapq
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones_inv = [-elem for elem in stones]
        heapq.heapify(stones_inv)
        result = 0
        while len(stones_inv)>=2:
            largest = heapq.heappop(stones_inv)
            sec_largest = heapq.heappop(stones_inv)
            if largest!= sec_largest:
                new = largest - sec_largest
                heapq.heappush(stones_inv,new)
        if len(stones_inv)==1:
            result = -stones_inv[0]
        return result
        