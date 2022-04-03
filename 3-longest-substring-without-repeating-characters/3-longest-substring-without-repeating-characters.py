class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        dim = len(s)
        if dim <= 1:
            #print("This is a trivial input with length ", dim)
            return dim
        else:
            start_idx = 0
            end_idx = 0
            win_slide = {}
            result = 0
            while end_idx <= dim - 1:
                #print("---------Trigger a while loop, start index = ",start_idx,", end index = ",end_idx)
                right_val = s[end_idx]
                #print("Substring repository = ", win_slide)
                #print("Updated substring length = ",result)
                #print("Check if ",s[end_idx]," exist in ",win_slide)
                if not (right_val in win_slide):
                    result = max(result,end_idx - start_idx+1)
                    win_slide[right_val]=end_idx
                    end_idx += 1
                    #print("No duplicates found, update substring repository = ", win_slide)
                    #print("#########Exit loop, start index = ",start_idx,", end index = ",end_idx,"\n")
                else:
                    location_of_dup = win_slide[right_val]
                    #print("Duplicate found in ",location_of_dup)
                    #print("Update substring repository ",win_slide)
                    for t in s[start_idx:location_of_dup+1]:
                        del win_slide[t]
                    win_slide[right_val] = end_idx
                    #print("Updated substring repository = ", win_slide)
                    #print("Updated substring repository ",win_slide)
                    start_idx = location_of_dup+1
                    end_idx += 1
                    #print("#########Exit loop, start index = ",start_idx,", end index = ",end_idx,"\n")
            return result
            
                
        