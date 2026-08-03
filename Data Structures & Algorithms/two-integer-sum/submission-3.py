class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dummy = sorted(nums)
        i=0 
        j=len(nums)-1

        while i<j:
            if (dummy[i]+dummy[j]) == target:
                a = nums.index(dummy[i])
                nums[a] = 'a'
                b = nums.index(dummy[j])
                if a<b:
                    return [a,b]
                else:
                    return [b,a]
            elif (dummy[i]+dummy[j]) < target:
                i+=1
            else:
                j-=1

        return False