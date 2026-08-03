from collections import Counter
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        dict1 = Counter(s)
        dict2 = Counter(t)

        if len(s)!=len(t):
            return False
            
        for key in dict1.keys():
            if key in dict2:
                if dict1[key] != dict2[key]:
                    return False

            else:
                return False

        return True