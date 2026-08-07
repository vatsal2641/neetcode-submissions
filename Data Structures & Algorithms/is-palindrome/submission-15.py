class Solution:
    def isPalindrome(self, s: str) -> bool:
        if len(s)==0 or len(s)==1:
            return True
        
        while len(s) and not s[0].isalnum():
            s = s[1:]
        
        while len(s) and not s[-1].isalnum():
            s = s[:-1]
        
        if len(s)==0 or len(s)==1:
            return True
            
        return (s[0].lower()==s[-1].lower()) and self.isPalindrome(s[1:-1])