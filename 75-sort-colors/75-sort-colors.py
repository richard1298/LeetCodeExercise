class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        def quicksort(nums,start = 0, stop = None):
            stop1 = stop if stop is not None else len(nums) - 1
            if stop1-start+1 >=2:
                pivot = nums[start]
                i = start
                j = start + 1
                stop1 = stop if stop is not None else len(nums) - 1
        #        print('********************this piece is to sort', nums[start:stop1+1],'***********************')
                while j <= stop1:
        #            print('#########start nums = ',nums)
        #            print('check nums[',j,']=',nums[j])
                    if nums[j] < pivot and i == start:
        #                print('DONOT NEED SWITCH!!')
                        j+=1
                    elif nums[j]>=pivot and i == start:
        #                print('DONOT NEED SWITCH!!')
                        i = j
                        j += 1
                    elif nums[j]<= pivot and i != start:
        #                print('NEED SWITCH!!')
                        nums[i], nums[j] = nums[j], nums[i]
                        i+= 1
                        j+= 1
                    else:
        #                print('DONOT NEED SWITCH!!')
                        j+= 1
        #            print('first index that is larger than or equal to pivot =',i)
        #            print('#########updated nums = ', nums)
        #            print('')
                if i == start:
                    nums[start], nums[stop1] = nums[stop1], nums[start]
                else:
                    nums[start], nums[i-1] = nums[i-1], nums[start]
        #        print('switch pivot:',nums)
        #        print('final i =',i)
                pivot = i
        #        print('left part = ',nums[start:pivot-1])
        #        print('right part = ', nums[pivot:stop1+1])
                quicksort(nums,start,pivot-2)
                quicksort(nums,pivot,stop1)
                return
            else:
                return
        quicksort(nums)