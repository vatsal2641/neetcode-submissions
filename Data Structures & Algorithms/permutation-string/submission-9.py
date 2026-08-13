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
        count_o = [0]*26
        curr_str = larger[0:k]

        for c in curr_str:
            count_o[ord(c)-ord('a')]+=1
        
        for i in range(n-k+1):
            indicator = True
            
            if count_s==count_o: 
                found = True

            
            count_o[ord(larger[i]) - ord('a')]-=1
            if i == (n-k):
                continue
            count_o[ord(larger[i+k]) - ord('a')]+=1

           
        if found == True:
            return True
        else: 
            return False
