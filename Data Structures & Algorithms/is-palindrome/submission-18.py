class Solution:
    def isPalindrome(self, s: str) -> bool:
        if len(s)==0 or len(s)==1:
            return True
        i = 0 
        j= len(s)-1

        while i<j:
            while i<j and not s[i].isalnum():
                i+=1
        
            while i<j and not s[j].isalnum():
                j-=1

            if i>=j:
                return True

            if s[i].lower()==s[j].lower():
                i+=1 
                j-=1
            else:
                return False
        
        return True