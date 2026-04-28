class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # sliding window
        # shift our r pointer and calculate the max profit
        
        maxProfit = 0
        l, r = 0, 1
        # since it's a sliding window problem we use while loop for mroe control
        # over poitners I think
        while r < len(prices):
            if prices[r] > prices[l]:
                profit = prices[r] - prices[l]
                maxProfit = max(maxProfit, profit)
            else:
                l = r
                
            r += 1

        return maxProfit