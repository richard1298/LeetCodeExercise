class Solution:
    def longestNiceSubstring(self, s: str) -> str:
        def nicecheck(key,l):
            #this function check if the upper/lower case exist in l
            to_upper = key.upper()
            to_lower = key.lower()
            is_upper = (key == to_upper)
            is_lower = (key == to_lower)
            if is_upper:
                if to_lower in l:
                    return True
                else:
                    return False
            else:
                if to_upper in l:
                    return True
                else:
                    return False
        dim = len(s)
        window = dim
        result = ''
        while window>0:
            #print('check window length=',window)
            isnice = True
            for i in range(dim-window+1):
                temp = s[i:i+window]
                #print('****substring slice=',temp)
                #print('****i=',i)
                j = 0
                while j <= len(temp)-1:
                    #print('****j=',j)
                    #print('****check character',temp[j],'in substring slice',temp)
                    isnice = isnice and nicecheck(temp[j],temp)
                    #print('****character',temp[j],'is',isnice)
                    if isnice == False:
                        break
                    j+=1
                if isnice == True:
                    #print('****substring slice=',temp,'is',isnice)
                    result = temp
                    break
                else:
                    #print('****substring slice=',temp,'is',isnice)
                    isnice = True
            if result != '':
                break
            else:
                window -= 1
            #print('update window=',window)
        return result
        