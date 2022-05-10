class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        a = list(set(nums1))
        b = list(set(nums2))
        rep = {}
        result = []
        for i in range(len(a)):
            rep[a[i]]=i
        for j in range(len(b)):
            if b[j] in rep:
                result.append(b[j])
        return result