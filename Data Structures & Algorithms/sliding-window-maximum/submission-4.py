class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        ans = []
        n = len(nums)
        queue = deque()
    
        for j in range(k):
            if len(queue)>0:
                while len(queue) and queue[-1]<nums[j]:
                    queue.pop()
                queue.append(nums[j])
                
            else:
                queue.append(nums[j])
        
        maxi = queue[0]
        ans.append(maxi)

        for i in range(1, n-k+1): 
            if maxi == nums[i-1]:
                queue.popleft()
               
            while len(queue) and queue[-1]<nums[i+k-1]:
                queue.pop()
                
            queue.append(nums[i+k-1])

            maxi = queue[0]
            ans.append(maxi)
            
        return ans
