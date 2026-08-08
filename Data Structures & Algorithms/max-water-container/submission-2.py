class Solution:
    def maxArea(self, heights: List[int]) -> int:
        n = len(heights)
        i = 0
        j = n-1
        ans = 0
        curr = 0
        while i<j:
            width = j-i
            height = min(heights[i], heights[j])
            curr = width*height
            ans = max(ans,curr)

            if (heights[i]< heights[j]):
                i+=1
            elif (heights[i]> heights[j]):
                j-=1

            else:
                i+=1
                j-=1
        return ans
                
