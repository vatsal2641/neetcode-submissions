class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        arr = []
        arr.append(1)
        arr_r = []
        arr_r.append(1)
        n = len(nums)
        for i in range(1, len(nums)):
            arr.append(arr[i-1]*nums[i-1])
            arr_r.append(arr_r[i-1]*nums[n-i])
        arr_r = arr_r[::-1]
        final_ans = []
        for i in range(len(arr_r)):
            final_ans.append(arr[i]*arr_r[i])
        return final_ans