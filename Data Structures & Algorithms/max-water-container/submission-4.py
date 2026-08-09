class Solution:
    def maxArea(self, heights: List[int]) -> int:
        n = len(heights)
        i = 0
        j = n-1
        ans = 0
        curr_water = 0
        while i<j:
            min_height = min(heights[i], heights[j])
            curr_water = min_height * (j-i)
            ans = max(ans, curr_water)

            if heights[i]<heights[j]:
                i+=1
            elif heights[i]>heights[j]:
                j-=1
            else:
                i+=1
                j-=1
        
        return ans
