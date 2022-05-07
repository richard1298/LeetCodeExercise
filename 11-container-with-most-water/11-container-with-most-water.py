class Solution:
    def maxArea(self, height: List[int]) -> int:
        start = 0
        end = len(height)-1
        area = 0
        result = 0
        while start < end:
            #print("start = ",start,", end = ", end)
            area = min(height[start],height[end]) * (end-start)
            #print("Area = ",area)
            result = max(result,area)
            if height[start] <= height[end]:
                start +=1
            else:
                end -=1
        return result
            