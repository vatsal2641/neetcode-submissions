class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0
        
        visit = set()
        pattern_t_word = collections.defaultdict(list)

        wordList.append(beginWord)

        for word in wordList:
            for j in range(len(word)):
                patt = word[:j] + "*" + word[j+1:]
                pattern_t_word[patt].append(word)

        q = deque()
        q.append(beginWord)

        visit.add(beginWord)

        result = 0
        while q:
            
            result+=1 

            for i in range(len(q)):      # For words at result==1 or 2 or 3 or 4 or 5
                word_req = q.popleft()

                if word_req == endWord:
                    return result

                for i in range(len(word_req)):
                    pat = word_req[:i]+"*"+word_req[i+1:]
                    for w in pattern_t_word[pat]:
                        if w not in visit:
                            q.append(w)
                            visit.add(w)
        
        return 0    #If endword could not be reached. 