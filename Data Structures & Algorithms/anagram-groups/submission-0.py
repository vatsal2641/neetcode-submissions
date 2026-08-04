from collections import Counter
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dict_ = {}
        overall_ans = []
        for i in range(len(strs)):
            if strs[i] == 0:
                continue
            ans = []
            ans.append(strs[i])
            for j in range(i+1, len(strs)):
                if strs[j] == 0:
                    continue
                if Counter(strs[i])==Counter(strs[j]):
                    ans.append(strs[j])
                    strs[j] = 0
            overall_ans.append(ans)
        return overall_ans