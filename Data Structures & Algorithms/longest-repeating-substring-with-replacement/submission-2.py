class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        store = defaultdict(int)
        i=0
        curr = 0
        ans = 0
        for j in range(len(s)):
            if store[s[j]]:
                store[s[j]]+=1
            else:
                store[s[j]]=1
            dict_val_lis = list(store.values())
            max_n = max(dict_val_lis)
            sum_extra = sum(dict_val_lis) - max_n

            while sum_extra>k:
                store[s[i]]-=1
                i+=1
                dict_val_lis = list(store.values())
                max_n = max(dict_val_lis)
                sum_extra = sum(dict_val_lis) - max_n


            curr= j-i+1
            ans = max(ans,curr)

        return ans



            
