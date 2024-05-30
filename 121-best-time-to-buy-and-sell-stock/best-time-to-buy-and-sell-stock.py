class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_s = prices[0]
        max_p = 0

        for pric in prices[1:]:
            min_s = min(pric,min_s)
            max_p = max(max_p,pric-min_s)
        return max_p