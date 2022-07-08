class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        def binsearch_helper(num, target):
            # this function find the first index that is equal to or larger than the target
            if num[-1] < target:
                return -1
            else:
                l, r = 0, len(num) - 1
                while l <= r:
                    mid = (l + r) // 2
                    if num[mid] < target:
                        l = mid + 1
                    else:
                        if mid > 0:
                            if num[mid - 1] < target:
                                break
                            else:
                                r -= 1
                        else:
                            break
                if numbers[mid] == target:
                    while mid < len(numbers)-1:
                        if numbers[mid+1] == target:
                            mid += 1
                        else:
                            break
                return mid

        l = 0
        r = len(numbers) - 1
        while l <= r:
            #print('start l =',l,'start r =',r)
            idx = binsearch_helper(numbers[0:r+1], target - numbers[l])
    #        print('binsearchindex =',idx)
            if idx == -1:
                l += 1
     #           print('end l =', l, 'end r =', r)
            else:
                if numbers[l] + numbers[idx] == target:
                    r = idx
                    break
                else:
                    r =idx - 1
                    l += 1
     #               print('end l =', l, 'end r =', r)
        result = [l + 1, r + 1]
        result.sort()
        return result
        
        