from collections import Counter
class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        dict={}
        item_counts = Counter(nums)
        for val in item_counts.values():
            if val>1:
                return True
        
        return False