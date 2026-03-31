class Solution:
    def findDuplicate(self, paths: List[str]) -> List[List[str]]:
        d = defaultdict(list)

        for s in paths:
            s = s.split()
            root = s[0]

            for file in s[1:]:
                start = file.index('(')
                d[file[start:]].append(root+'/'+file[:start])

        return [x for x in d.values() if len(x)>1]