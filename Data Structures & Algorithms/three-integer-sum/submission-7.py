class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        length = len(nums)
        ans = []
        
        for i in range(len(nums)-2):
            if i>0 and (nums[i]==nums[i-1]):
                continue
            m = i+1
            l = length-1

            while m<l:
                sums = (nums[i]+nums[m]+nums[l])
                if sums == 0:
                    ans.append([nums[i],nums[m],nums[l]])
                    m+=1       # imp 
                    l-=1       # imp
                    while l>m and (nums[l] == nums[l+1]):
                        l-=1
                    while m<l and (nums[m]==nums[m-1]):
                        m+=1
                elif sums > 0:
                    
                    l-=1

                else:
        
                    m+=1
            
        return ans
        