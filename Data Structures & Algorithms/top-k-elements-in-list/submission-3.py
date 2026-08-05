from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = Counter(nums)
        count = dict(sorted(count.items(), reverse=True, key= lambda x:x[1]))
        return list(count.keys())[:k]