class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        #The idea is to use hashmap for a faster search; drawback is extra memory
        #Algorithm: create a dictionary from the first elem up till the previous elem;if target - current elem exists in the dictionary, return; otherwise expand the dictionary
        search_dict = {}
        for index, val in enumerate(nums):
            if target - val in search_dict:
                return [search_dict[target - val],index]
            else:
                search_dict[val] = index
                
            