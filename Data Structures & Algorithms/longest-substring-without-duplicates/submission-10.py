class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if s.isspace():
            return 1
        
        n = len(s)
        repeating_check = defaultdict()
        if n>1:
            i = 0
            j = 0
            prev_i=0
            curr_len = 1
            ans_len = 0
            while j<n:
                ele = s[j]
                if ele in repeating_check:
                    i = repeating_check[ele]+1
                repeating_check[ele]=j
                if i<prev_i:
                    i = prev_i
                curr_len = (j-i)+1
                ans_len=max(ans_len, curr_len)
                j+=1
                prev_i = i
            return ans_len

        else:
            return n
        


