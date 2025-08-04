class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        n = len(fruits)
        l = 0
        r = 0
        hmap = {}
        ans = 0
        while r<n:
            hmap[fruits[r]] = hmap.get(fruits[r],0)+1
            r += 1
            # print(fruits[l:r])
            while len(hmap)>2:
                rem = fruits[l]
                hmap[rem] -=1
                if hmap[rem] == 0:
                    del hmap[rem]
                l += 1
            # print(fruits[l:r])
            ans = max(ans,r-l)
        return ans
        