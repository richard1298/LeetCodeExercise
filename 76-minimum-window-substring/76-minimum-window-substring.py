class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(s) < len(t):
            result = ''
        else:
            t1 =''.join(list(set(t)))
            need = {}
            have = {}
            i, j = 0, len(t)-1
            for elem in t1:
                need[elem] = t.count(elem)
                have[elem] = s[i:j+1].count(elem)
    #        print(need)
    #        print(have)
            def judge(already,benchmark):
                #this is a helper function that judges if the already have dictionary satisfies benchmark
                result = True
                for elem in benchmark:
                    result = result and already[elem] >= benchmark[elem]
                    if result == False:
                        break
                return result

            result = ''
            minwindow = float('inf')
            while j <=len(s)-1:
    #            print('this_substring =',s[i:j+1])
    #            print('have=',have)
    #            print('need=',need)
    #            print('judge=',judge(have,need))
                if judge(have,need) == False:
    #                print('this substring is not good')
                    if j+1 <= len(s) - 1:
                        if s[j+1] in need.keys():
                            have[s[j+1]] += 1
                    j+= 1
                else:
    #                print('this substring is good')
                    while judge(have,need):
                        if j - i + 1 < minwindow:
                            result = s[i:j + 1]
                            minwindow = j - i + 1
                        if s[i] in need.keys():
                            have[s[i]] -= 1
                        i += 1
        return result