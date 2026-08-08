class Solution:
    def trap(self, height: List[int]) -> int:
        max_left = []
        max_right = []
        n = len(height)
        max_val = height[0]
        max_left.append(height[0])
        for i in range(1,n):
            max_val = max(max_val, height[i])
            max_left.append(max_val)
        
        max_val = height[n-1]
        max_right.append(height[n-1])
        for j in range(n-2, -1, -1):
            max_val = max(max_val, height[j])
            max_right.append(max_val)
        max_right = max_right[::-1]

        ans = 0
        for i in range(n):
            ans+= (min(max_left[i], max_right[i])- height[i])
        return ans
