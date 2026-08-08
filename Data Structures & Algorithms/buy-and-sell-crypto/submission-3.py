class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        mini = float('inf')
        ans = 0
        for sell in prices:
            if mini == float('inf'):
                mini = sell
            
            if mini >sell:
                mini=sell
        
            diff = (sell-mini)
        
            ans = max(ans, diff)
        
        return ans
