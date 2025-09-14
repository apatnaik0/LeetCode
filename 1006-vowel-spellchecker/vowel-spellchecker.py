class Solution:
    def devowel(self,word):
        nword = ''
        for c in word:
            if c in 'aeiou':
                nword += '*'
            else:
                nword += c
        return nword

    def spellchecker(self, wordlist: List[str], queries: List[str]) -> List[str]:
        exact = set(wordlist)
        casemap = {}
        vowelmap = {}

        for w in wordlist:
            l = w.lower()
            d = self.devowel(l)
            if l not in casemap:
                casemap[l] = w
            if d not in vowelmap:
                vowelmap[d] = w
        
        ans = []
        for q in queries:
            if q in exact:
                ans.append(q)
            else:
                l = q.lower()
                d = self.devowel(l)
                if l in casemap:
                    ans.append(casemap[l])
                elif d in vowelmap:
                    ans.append(vowelmap[d])
                else:
                    ans.append('')
        return ans
