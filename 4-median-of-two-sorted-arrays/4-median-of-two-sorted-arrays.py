class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        shortlist, longlist = nums1, nums2
        total = len(nums1) + len(nums2)    
        #define the pivot index for the short array
        half = total//2
        if len(longlist) < len(shortlist):
            shortlist, longlist = longlist, shortlist
        l = 0
        r = len(shortlist) - 1
        while True:
            #get the partition of the short array 
            i = (l + r)//2 
            j = half - i - 2
            shortlist_left = shortlist[i] if i >=0 else -float('inf')
            shortlist_right = shortlist[i+1] if (i+1)<len(shortlist) else float('inf')
            longlist_left = longlist[j] if j >=0 else -float('inf')
            longlist_right = longlist[j+1] if (j+1)<len(longlist) else float('inf')
            #define four variables for easy reference:
            if shortlist_left<=longlist_right and longlist_left <= shortlist_right:
                if total%2:
                    return min(shortlist_right,longlist_right)
                else:
                    return (max(shortlist_left,longlist_left)+min(shortlist_right,longlist_right))/2
            elif shortlist_left > longlist_right:
                r = i - 1
            else:
                l = i + 1
        