class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        left = 0
        maxprofit = 0
        for right in range(len(prices)):
            while prices[left] > prices[right]:
                left = right
            buy = prices[left]
            sell = prices[right]
            maxprofit = max(maxprofit, sell - buy)
        return maxprofit