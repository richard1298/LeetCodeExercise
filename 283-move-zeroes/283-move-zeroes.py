class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
      
        idx = next((i for i, j in enumerate(nums) if j == 0), -1)
        if idx != -1:
            i = idx
            j = idx + 1
            while j <= len(nums) - 1:
                if nums[j] == 0:
                    j += 1
                else:
                    nums[i], nums[j] = nums[j], nums[i]
                    i += 1
                    j += 1
        