class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        n = len(nums)
        ans = []
        
        for i in range(n-2):
            if i>0 and nums[i] == nums[i-1]:
                continue

            mid = i+1
            end = n-1
            
            while mid < end:
                sums = nums[i] + nums[mid] + nums[end]
                if sums == 0:
                    ans.append([nums[i],nums[mid] , nums[end]])
                    mid += 1
                    end -= 1
                    while mid<end and (nums[mid] == nums[mid-1]):
                        mid+=1
                    while mid<end and (nums[end] == nums[end+1]):
                        end-=1 
                
                elif sums < 0:
                    mid+=1
                
                else :
                    end-=1
                
        return ans