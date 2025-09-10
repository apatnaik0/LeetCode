class Solution:
    def minimumTeachings(self, n: int, languages: List[List[int]], friendships: List[List[int]]) -> int:
        mini = float('inf')
        learn = set()
        for i,j in friendships:
            if set(languages[i-1]).intersection(set(languages[j-1]))==set():
                learn.update([i,j])
        # print(learn)
        for i in range(1,n+1):
            ct = 0
            for j in learn:
                if i not in languages[j-1]:
                    ct += 1
            mini = min(mini,ct)
        return mini