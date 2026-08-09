class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        count_s = [0]*26
        
        if len(s1)<=len(s2):
            larger = s2
            smaller = s1
        else:
            return False
        
        for c in smaller: 
            count_s[ord(c)-ord('a')]+=1
        
        n = len(larger)
        k = len(smaller)

        found = False
        
        for i in range(n-k+1):
            count_o = [0]*26
            curr_str = larger[i:i+k]
            indicator = True
            for c in curr_str:
                count_o[ord(c)-ord('a')]+=1
            for i in range(26):
                if count_s[i]!=count_o[i]:
                    indicator = False
            
            if indicator == False:
                continue
            else: 
                found = True
        
        if found == True:
            return True
        else: 
            return False



