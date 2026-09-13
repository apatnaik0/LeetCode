class Solution:
    def largestOverlap(self, img1: List[List[int]], img2: List[List[int]]) -> int:
        ones_img1 = []
        ones_img2 = []
        n = len(img1)

        for i in range(n):
            for j in range(n):
                if img1[i][j]==1:
                    ones_img1.append((i,j))
                if img2[i][j]==1:
                    ones_img2.append((i,j))

        freq = defaultdict(int)

        for r1,c1 in ones_img1:
            for r2,c2 in ones_img2:
                dr = r1-r2
                dc = c1-c2

                freq[(dr,dc)] += 1

        return max(freq.values(),default=0)

        