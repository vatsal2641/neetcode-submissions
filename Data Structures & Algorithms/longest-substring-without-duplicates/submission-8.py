class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        curr = 0
        ans = 0
        prev_start =0
        start=0
        end=0
        if s.isspace():
            return 1
        s = s.strip()
        if len(s)>1:
            dic_win = defaultdict()
            dic_win[s[0]] = 0
            for i in range(1,len(s)):
                if s[i] not in dic_win:
                    dic_win[s[i]] = i
                else:
                    start = dic_win[s[i]]+1
                    if start<prev_start:
                        start = prev_start
                    dic_win[s[i]] = i
                
                curr = (i-start)+1
                prev_start = start
                ans = max(ans,curr)
            return ans
        
        else:
            return len(s)

