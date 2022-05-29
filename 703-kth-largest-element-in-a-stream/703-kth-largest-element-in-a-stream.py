class KthLargest:
    import heapq
    def __init__(self, k: int, nums: List[int]):
        self.val = nums
        self.order = k
        heapq.heapify(self.val)
        while len(self.val)>k:
            heapq.heappop(self.val)

    def add(self, val: int) -> int:
        heapq.heappush(self.val,val)
        if len(self.val)>self.order:
            heapq.heappop(self.val)
        return self.val[0]
        


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)