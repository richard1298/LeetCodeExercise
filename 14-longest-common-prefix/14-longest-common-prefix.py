class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        dim = min(list(map(len,strs)))
        #dim is the minimum length of the substring of the input list
        if dim ==0:
            return ""
        else:
            j = 0
            match = True
            while j<=dim - 1:
                temp = [elem[j] for elem in strs]
                #print("temp=",temp)
                match = (len(set(temp))==1)
                #print("match=",match)
                if match:
                    j+= 1
                else:
                    break
                #print("updated j=",j)
            pref = strs[0]
            return pref[0:j]
