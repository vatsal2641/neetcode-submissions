class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        set_list = set(nums)
        res_count = 1
        if len(nums) == 0:
            return 0
        for i in set_list:

            curr_count = 1
            if i-1 in set_list:
                continue
            else: 
                while (i+1) in set_list:
                    i+=1
                    curr_count+=1
            
            res_count = max(res_count, curr_count)

        return res_count

