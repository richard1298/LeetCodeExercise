class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l, r = 0, 1
        profit = 0
        buyprice = prices[0]
        while r <= len(prices)-1:
            if prices[l]<prices[r]:
                profit = max(profit,prices[r]-prices[l])
                r+=1
            else:
                l=r
                r+=1
        return profit