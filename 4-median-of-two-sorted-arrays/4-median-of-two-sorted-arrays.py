class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        if len(nums1) ==0:
            return nums2[len(nums2)//2] if len(nums2)%2 == 1 else 0.5*(nums2[len(nums2)//2]+nums2[len(nums2)//2-1])
        elif len(nums2) == 0:
            return nums1[len(nums1) // 2] if len(nums1) % 2 == 1 else 0.5 * (
                        nums1[len(nums1) // 2] + nums1[len(nums1) // 2 - 1])
        else:
            if len(nums1) > len(nums2):
                nums1, nums2 = nums2, nums1
            l, r = 0, len(nums1) - 1
            while True:
                mid = (l + r) // 2

                part2 = (len(nums1) + len(nums2)) // 2 - (mid + 1)
                nums1_left = nums1[mid] if mid >= 0 else -float('inf')
                nums1_right = nums1[mid + 1] if mid + 1 <= len(nums1) - 1 else float('inf')
                nums2_left = nums2[part2 - 1] if part2 - 1 >= 0 else -float('inf')
                nums2_right = nums2[part2] if part2<=len(nums2)-1 else float('inf')
                #print('nums1_left=',nums1_left,'nums1_right=',nums1_right)
                #print('nums2_left=', nums2_left, 'nums2_right=', nums2_right)
                if max(nums1_left, nums2_left) <= min(nums1_right, nums2_right):
                    # the correct partition is found
                    break
                elif nums2_left > nums1_right:
                    l = mid + 1
                else:
                    r = mid - 1
            if (len(nums1) + len(nums2)) % 2 == 1:
                return min(nums1_right, nums2_right)
            else:
                return 0.5 * (max(nums1_left, nums2_left) + min(nums1_right, nums2_right))