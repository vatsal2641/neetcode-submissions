class Solution:

    def encode(self, strs: List[str]) -> str:
        str_ = ""
        for s in strs:
            str_ += str(len(s))+"#"+s
        return str_
    def decode(self, s: str) -> List[str]:
        i = 0
        ans=[]
        while i<len(s):
            j=i
            while s[j]!="#":
                j+=1
            num = int(s[i:j])
            ans.append(s[(j+1):(j+1+num)])
            i=(j+num+1)
        
        return ans
