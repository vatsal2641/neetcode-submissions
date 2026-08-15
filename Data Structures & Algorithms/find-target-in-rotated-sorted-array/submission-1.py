class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if len(nums)==1:
            if target == nums[0]:
                return 0
            else: 
                return -1
            
        else: 
            l = 0
            h = len(nums) - 1

            while l<=h:
                mid = (l+h)//2

                if nums[mid] == target:
                    return mid

                elif nums[l]<=nums[mid]:
                    if target <= nums[mid] and target>=nums[l]:
                        h = mid-1
                    else:
                        l= mid+1

                else:
                    if target >= nums[mid] and target<=nums[h]:
                        l = mid +1
                    else:
                        h = mid -1

        return -1
