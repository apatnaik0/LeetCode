class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        wordSet = set(wordList)
        if endWord not in wordSet:
            return 0

        q = deque()
        q.append((beginWord,1))

        while q:
            word,d = q.popleft()
            if word == endWord:
                return d
            
            for i in range(len(word)):
                for j in range(26):
                    newWord = word[:i] + chr(ord('a')+j) + word[i+1:]
                    if newWord in wordSet:
                        q.append((newWord,d+1))
                        wordSet.remove(newWord)
            
        return 0
        
