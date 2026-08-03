class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        from collections import Counter
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        dict1 = Counter(s)
        dict2 = Counter(t)

        if len(s)!=len(t):
            return False
            
        return dict1 == dict2