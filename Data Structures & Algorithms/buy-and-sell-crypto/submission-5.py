class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        ans = 0
        n = len(prices)
        mini = prices[0]
        for i in range(1, n):
            diff = (prices[i]-mini)
            ans= max(diff, ans)
            if mini > prices[i]:
                mini = prices[i]
            
        return ans
