class Solution:
    def findMin(self, nums: List[int]) -> int:
        
        n = len(nums)
        if (len(nums) == 1) or nums[0]<nums[-1]:
            return nums[0]
        
        elif len(nums)==2:
            return min(nums)

        elif nums[0]<nums[n-2]:
            return nums[-1]
        
        else:
            l = 0
            h = len(nums)-1

            while l<=h:
                mid = (l+h)//2
                if nums[mid] < nums[mid+1] and nums[mid] < nums[mid-1]:
                    return nums[mid]
                else:
                    if nums[h]>nums[mid]:
                        h = mid - 1
                    
                    else:
                        l = mid+1
            
        


            
