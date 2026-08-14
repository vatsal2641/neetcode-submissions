import math
class Solution:
    def total_time(self, piles, rate):
        total_time = 0
        for i in range(len(piles)):
            total_time += math.ceil(piles[i]/rate)

        return total_time

    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        
        min_r = 1
        max_r = max(piles)
        
        low = max_r
        high = min_r

        final_rate = float('inf')
# We have to run the loop on rate because final answer would be on rate but comparison is on time, so we convert to time and then compare although we run the BS on rate. 

        while low>=high:

            mid_rate = (low+high)//2

            mid_time = self.total_time(piles, mid_rate)

                        

            
            if mid_time <= h :
                final_rate = min(final_rate, mid_rate)
                low = mid_rate - 1 
            else:
                high = mid_rate + 1

            
        return final_rate




