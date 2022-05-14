class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        n, m = len(image), len(image[0])
        for i in range(n):
            l, r = 0, m - 1
            temp = image[i]
            while l <= r:
                temp[l], temp[r] = 1-temp[r], 1-temp[l]
                l+=1
                r-=1
        return image