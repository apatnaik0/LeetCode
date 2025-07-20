class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0
        wordset = set(wordList)
        q = deque()
        q.append([beginWord,1])

        while q:
            word,d = q.popleft()
            if word == endWord:
                return d
            for i in range(len(word)):
                for j in range(26):
                    newword = word[:i]+chr(ord('a')+j)+word[i+1:]
                    if newword in wordset:
                        wordset.remove(newword)
                        q.append([newword,d+1])
        return 0
        