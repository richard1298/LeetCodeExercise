class Solution:
    import heapq
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        s = score
        dic = {}
        s=[-elem for elem in s]
        heapq.heapify(s)
        first = -heapq.heappop(s)
        dic[first] = 'Gold Medal'
        if len(score)>1:
            second = -heapq.heappop(s)
            dic[second] = 'Silver Medal'
        if len(score)>2:
            third = -heapq.heappop(s)
            dic[third] = 'Bronze Medal'
        i = 4
        while len(s)>0:
            temp = -heapq.heappop(s)
            dic[temp] = str(i)
            i+=1
        #print(dic)
        result = [dic[elem] for elem in score]
        return result