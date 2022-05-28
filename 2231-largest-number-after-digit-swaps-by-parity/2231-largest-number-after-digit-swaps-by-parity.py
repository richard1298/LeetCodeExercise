class Solution:
    import heapq
    def largestInteger(self, num: int) -> int:
        l = list(str(num))
        l = [int(elem) for elem in l]
        s = [1 if elem%2 == 1 else 0 for elem in l]
        odd = []
        even = []
        result = []
        #print('l=',l)
        #print('s=',s)
        for i in range(len(s)):
            if s[i] == 1:
                odd.append(-l[i])
            else:
                even.append(-l[i])
        #print('odd=',odd)
        #print('even=',even)
        if odd != []:
            heapq.heapify(odd)
        if even !=[]:
            heapq.heapify(even)
        #print('odd=',odd)
        #print('even=',even)

        for i in range(len(s)):
            if s[i]==1:
                temp = -heapq.heappop(odd)
                #print('odd list after removed=',odd)
                result.append(str(temp))
            else:
                temp = -heapq.heappop(even)
                #print('even list after removed=',even)
                result.append(str(temp))
        return int(''.join(result))
        
            
            
            