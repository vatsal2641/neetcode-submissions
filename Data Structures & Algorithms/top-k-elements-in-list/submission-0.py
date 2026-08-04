from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        ans_list = []
        count_dict = Counter(nums)
        sorted_dict = dict(sorted(count_dict.items(), reverse=True, key=lambda x:x[1]))
        ans_list = list(sorted_dict.keys())
        return ans_list[:k]