class Solution:
    def dfs(self,word,seq,mp,beginWord,ans):
        print(word,seq)
        if word == beginWord:
            ans.append(seq[::-1])
            return
        
        for i in range(len(word)):
            for j in range(26):
                newword = word[:i]+chr(ord('a')+j)+word[i+1:]
                if newword in mp and mp[newword]+1 == mp[word]:
                    seq.append(newword)
                    self.dfs(newword,seq,mp,beginWord,ans)
                    seq.pop()


    def findLadders(self, beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:

        def dfs(word,seq,mp,beginWord,ans):
            print(word,seq)
            if word == beginWord:
                ans.append(seq[::-1])
                return
            
            for i in range(len(word)):
                for j in range(26):
                    newword = word[:i]+chr(ord('a')+j)+word[i+1:]
                    if newword in mp and mp[newword]+1 == mp[word]:
                        seq.append(newword)
                        dfs(newword,seq,mp,beginWord,ans)
                        seq.pop()
                        
        if endWord not in wordList:
            return []
        wordset = set(wordList)
        q = deque()
        q.append([beginWord,0])
        mp = dict()
        mp[beginWord]=0
        wordset.discard(beginWord)
        while q:
            word,steps = q.popleft()
            if word == endWord:
                break
            for i in range(len(word)):
                for j in range(26):
                    newword = word[:i]+chr(ord('a')+j)+word[i+1:]
                    if newword in wordset:
                        q.append([newword,steps+1])
                        mp[newword] = steps+1
                        wordset.remove(newword)
        print(mp)
        ans = []
        if endWord in mp.keys():
            dfs(endWord,[endWord],mp,beginWord,ans)
        return ans
        
