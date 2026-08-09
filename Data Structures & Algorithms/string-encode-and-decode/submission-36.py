class Solution:

    def encode(self, strs: List[str]) -> str:

        encoded_str=""

        for str_ in strs:
            length = len(str_)
            encoded_str+=str(length) + '#' + str_
        return encoded_str

    def decode(self, s: str) -> List[str]:

        i = 0
        j = 0
        ans = []
        n = len(s)
        while j<n:
            while s[j]!= '#':
                j+=1
            start = j+1
            to_skip = int(s[i:j])
            j+=(to_skip+1)
            end = j
            ans.append(s[start:end])
            i=j
        return ans
