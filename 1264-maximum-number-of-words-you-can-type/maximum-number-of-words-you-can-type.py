class Solution:
    def canBeTypedWords(self, text: str, brokenLetters: str) -> int:
        broken = set(brokenLetters)
        count = 0
        for word in text.split():
            for c in word:
                if c in broken:
                    count += 1
                    break
        return len(text.split())-count
        