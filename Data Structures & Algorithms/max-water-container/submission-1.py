class Solution:
    def maxArea(self, heights: List[int]) -> int:
        max_val = 0
        max_array_l = []
        for i in range(len(heights)):
            max_val = max(max_val, heights[i])
            max_array_l.append(max_val)

        max_val = 0
        max_array_r = []
        for i in range(len(heights)-1,-1,-1):
            max_val = max(max_val, heights[i])
            max_array_r.append(max_val)   
        max_array_r = max_array_r[::-1]

        n = len(heights)
        ans = 0
        for start in range(n-1):
            if start>0 and (max_array_l[start]==max_array_l[start-1]):
                continue
            
            end = n-1
            curr = 0
            while end>start:
                if start<end and end<(n-1) and (max_array_r[end]==max_array_r[end+1]):
                    end-=1
           

                curr = (end - start)*min(max_array_l[start], max_array_r[end])
                end-=1
                ans = max(ans, curr)

        return ans
